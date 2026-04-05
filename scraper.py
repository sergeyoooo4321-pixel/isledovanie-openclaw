#!/usr/bin/env python3
"""OpenClaw Use Cases Research Scraper"""

import os
import sys
import json
import time
import traceback
from datetime import datetime
from pathlib import Path

# --- Config ---
BASE_DIR = Path(__file__).parent
RAW_DIR = BASE_DIR / "raw"
META_DIR = BASE_DIR / "meta"
RAW_DIR.mkdir(exist_ok=True)
META_DIR.mkdir(exist_ok=True)

ERRORS_LOG = META_DIR / "errors.log"
SOURCES_JSON = META_DIR / "sources.json"

NOW = datetime.now().strftime("%Y-%m-%d %H:%M")

# --- Sources ---
BLOG_SOURCES = [
    ("01_showcase_openclaw_ai.md", "https://openclaw.ai/showcase", "OpenClaw Showcase"),
    ("02_usecases_openclaw_rocks.md", "https://openclaw.rocks/blog/openclaw-use-cases", "OpenClaw Rocks - Use Cases"),
    ("03_usecases_openclaw_com_au.md", "https://openclaw.com.au/use-cases", "OpenClaw AU - Use Cases"),
    ("04_remoteopenclaw_complete.md", "https://remoteopenclaw.com/blog/openclaw-use-cases-complete-guide", "RemoteOpenClaw - Complete Guide"),
    ("05_remoteopenclaw_what_can_it_do.md", "https://remoteopenclaw.com/blog/openclaw-use-cases-what-can-it-do", "RemoteOpenClaw - What Can It Do"),
    ("06_solvea_glossary.md", "https://solvea.cx/glossary/openclaw-use-cases", "Solvea - OpenClaw Use Cases"),
    ("07_sidsaladi_substack.md", "https://sidsaladi.substack.com/p/openclaw-101-2026-march-29-the-complete", "SidSaladi Substack - OpenClaw 101"),
    ("08_aiblewmymind_substack.md", "https://aiblewmymind.substack.com/p/openclaw-use-cases-guide", "AibleWMyMind Substack - Use Cases Guide"),
    ("09_theinteractive_studio.md", "https://insights.theinteractive.studio/openclaw-for-business-what-it-is-real-use-cases-and-how-to-implement-it", "TheInteractive Studio - OpenClaw for Business"),
    ("10_clawbot_blog_50.md", "https://www.clawbot.blog/blog/openclaw-50-real-world-use-cases-for-the-open-source-ai-agent-framework/", "ClawBot Blog - 50 Use Cases"),
    ("11_datacamp_projects.md", "https://www.datacamp.com/blog/openclaw-projects", "DataCamp - OpenClaw Projects"),
    ("12_kdnuggets.md", "https://www.kdnuggets.com/openclaw-explained-the-free-ai-agent-tool-going-viral-already-in-2026", "KDnuggets - OpenClaw Explained"),
    ("13_institutional_investor.md", "https://www.institutionalinvestor.com/article/openclaw-ai-agent-institutional-investors-need-understand-shouldnt-touch", "Institutional Investor - OpenClaw"),
]

GITHUB_SOURCES = [
    ("14_github_awesome_usecases.md", "https://raw.githubusercontent.com/hesamsheikh/awesome-openclaw-usecases/main/README.md", "GitHub Awesome OpenClaw Usecases"),
    ("15_github_openclaw_main.md", "https://github.com/openclaw/openclaw", "GitHub OpenClaw Main"),
    ("16_github_discussions.md", "https://github.com/openclaw/openclaw/discussions", "GitHub OpenClaw Discussions"),
]

REDDIT_SOURCES = [
    ("17_reddit_r_openclaw.md", "https://www.reddit.com/r/openclaw/top.json?limit=100&t=all", "Reddit r/openclaw"),
    ("18_reddit_r_openclawcentral.md", "https://www.reddit.com/r/OpenClawCentral/top.json?limit=100&t=all", "Reddit r/OpenClawCentral"),
    ("19_reddit_r_myclaw.md", "https://www.reddit.com/r/myclaw/top.json?limit=100&t=all", "Reddit r/myclaw"),
    ("20_reddit_r_openclawpirates.md", "https://www.reddit.com/r/openclawpirates/top.json?limit=100&t=all", "Reddit r/openclawpirates"),
    ("21_reddit_r_openclawdevs.md", "https://www.reddit.com/r/OpenClawDevs/top.json?limit=100&t=all", "Reddit r/OpenClawDevs"),
    ("22_reddit_search_usecase.md", "https://www.reddit.com/search.json?q=openclaw+use+case&sort=top&t=all&limit=100", "Reddit Search - openclaw use case"),
    ("23_reddit_search_howuse.md", "https://www.reddit.com/search.json?q=openclaw+how+i+use&sort=top&t=all&limit=100", "Reddit Search - how i use openclaw"),
    ("24_reddit_search_moltbot.md", "https://www.reddit.com/search.json?q=moltbot+clawdbot+use+case&sort=top&t=all&limit=100", "Reddit Search - moltbot clawdbot"),
]

OTHER_SOURCES = [
    ("25_clawhub_catalog.md", "https://clawhub.ai/chunhualiao/openclaw-usecase-catalog", "ClawHub - Use Case Catalog"),
    ("26_redditor_ai_blog.md", "https://www.redditor.ai/blog/openclaw-for-reddit-setup-use-cases-alternatives", "Redditor AI - OpenClaw for Reddit"),
    ("27_openclawroadmap.md", "https://openclawroadmap.com/about-community.php", "OpenClaw Roadmap Community"),
]

def log_error(filename, url, error_msg):
    with open(ERRORS_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{NOW}] {filename} | {url} | {error_msg}\n")

def save_md(filename, title, url, content, status="OK"):
    filepath = RAW_DIR / filename
    md = f"# {title}\n**URL:** {url}  \n**Дата сбора:** {NOW}  \n**Статус:** {status}  \n\n---\n\n{content}\n"
    filepath.write_text(md, encoding="utf-8")
    return filepath

def format_reddit_json(data):
    """Parse Reddit JSON response into readable markdown"""
    lines = []
    try:
        posts = data.get("data", {}).get("children", [])
        for i, post in enumerate(posts, 1):
            d = post.get("data", {})
            title = d.get("title", "No title")
            selftext = d.get("selftext", "")
            author = d.get("author", "unknown")
            score = d.get("score", 0)
            url = d.get("url", "")
            permalink = d.get("permalink", "")
            num_comments = d.get("num_comments", 0)
            subreddit = d.get("subreddit", "")

            lines.append(f"## {i}. {title}")
            lines.append(f"**Author:** u/{author} | **Score:** {score} | **Comments:** {num_comments} | **Subreddit:** r/{subreddit}")
            if permalink:
                lines.append(f"**Permalink:** https://www.reddit.com{permalink}")
            if url and url != f"https://www.reddit.com{permalink}":
                lines.append(f"**Link:** {url}")
            if selftext:
                lines.append(f"\n{selftext}")
            lines.append("\n---\n")
    except Exception as e:
        lines.append(f"Error parsing Reddit JSON: {e}")

    if not lines:
        return "No posts found or subreddit does not exist."
    return "\n".join(lines)


def scrape_with_playwright(sources):
    """Scrape blog/website sources using Playwright"""
    from playwright.sync_api import sync_playwright
    try:
        from markdownify import markdownify as md_convert
        has_markdownify = True
    except ImportError:
        has_markdownify = False

    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )

        for filename, url, title in sources:
            try:
                print(f"  Loading: {url}")
                page = context.new_page()
                page.goto(url, wait_until="networkidle", timeout=30000)
                time.sleep(1)

                # Get page content
                html = page.content()

                # Try to extract main content
                try:
                    body = page.query_selector("article") or page.query_selector("main") or page.query_selector("body")
                    text_content = body.inner_text() if body else page.inner_text("body")
                except:
                    text_content = page.inner_text("body")

                # Also try markdownify for better formatting
                if has_markdownify:
                    try:
                        md_content = md_convert(html, heading_style="ATX", strip=["script", "style", "nav", "footer"])
                        # Use markdown version if it's more substantial
                        if len(md_content) > len(text_content) * 0.5:
                            text_content = md_content
                    except:
                        pass

                save_md(filename, title, url, text_content, "OK")
                results.append({"file": filename, "url": url, "title": title, "status": "OK", "date": NOW, "size": len(text_content)})
                page.close()
                print(f"  -> OK ({len(text_content)} chars)")

            except Exception as e:
                err = str(e)[:200]
                print(f"  -> ERROR: {err}")
                log_error(filename, url, err)
                save_md(filename, title, url, f"ERROR: {err}", "ERROR")
                results.append({"file": filename, "url": url, "title": title, "status": "ERROR", "date": NOW, "error": err})
                try:
                    page.close()
                except:
                    pass

            time.sleep(2)

        browser.close()
    return results


def scrape_reddit(sources):
    """Scrape Reddit sources using requests + JSON API"""
    import requests

    results = []
    headers = {
        "User-Agent": "OpenClawResearchBot/1.0 (research project)"
    }

    for filename, url, title in sources:
        try:
            print(f"  Loading: {url}")
            resp = requests.get(url, headers=headers, timeout=30)
            resp.raise_for_status()

            data = resp.json()
            content = format_reddit_json(data)

            save_md(filename, title, url, content, "OK")
            results.append({"file": filename, "url": url, "title": title, "status": "OK", "date": NOW, "size": len(content)})
            print(f"  -> OK ({len(content)} chars)")

        except Exception as e:
            err = str(e)[:200]
            print(f"  -> ERROR: {err}")
            log_error(filename, url, err)
            save_md(filename, title, url, f"ERROR: {err}", "ERROR")
            results.append({"file": filename, "url": url, "title": title, "status": "ERROR", "date": NOW, "error": err})

        time.sleep(3)

    return results


def scrape_github_raw(sources):
    """Scrape GitHub sources using requests"""
    import requests
    try:
        from markdownify import markdownify as md_convert
        has_markdownify = True
    except ImportError:
        has_markdownify = False

    results = []
    headers = {
        "User-Agent": "OpenClawResearchBot/1.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }

    for filename, url, title in sources:
        try:
            print(f"  Loading: {url}")

            if "raw.githubusercontent.com" in url:
                # Direct raw content
                resp = requests.get(url, headers=headers, timeout=30)
                resp.raise_for_status()
                content = resp.text
            else:
                # GitHub page - use playwright for JS rendering
                # But first try with requests
                resp = requests.get(url, headers=headers, timeout=30)
                resp.raise_for_status()
                if has_markdownify:
                    content = md_convert(resp.text, heading_style="ATX", strip=["script", "style", "nav", "footer"])
                else:
                    from bs4 import BeautifulSoup
                    soup = BeautifulSoup(resp.text, "html.parser")
                    # Try to find readme content
                    readme = soup.find("article") or soup.find("div", {"id": "readme"})
                    content = readme.get_text(separator="\n") if readme else soup.get_text(separator="\n")

            save_md(filename, title, url, content, "OK")
            results.append({"file": filename, "url": url, "title": title, "status": "OK", "date": NOW, "size": len(content)})
            print(f"  -> OK ({len(content)} chars)")

        except Exception as e:
            err = str(e)[:200]
            print(f"  -> ERROR: {err}")
            log_error(filename, url, err)
            save_md(filename, title, url, f"ERROR: {err}", "ERROR")
            results.append({"file": filename, "url": url, "title": title, "status": "ERROR", "date": NOW, "error": err})

        time.sleep(2)

    return results


def main():
    print("=" * 60)
    print("  OpenClaw Use Cases Research Scraper")
    print(f"  Started: {NOW}")
    print("=" * 60)

    # Clear errors log
    ERRORS_LOG.write_text("", encoding="utf-8")

    all_results = []
    total = len(BLOG_SOURCES) + len(GITHUB_SOURCES) + len(REDDIT_SOURCES) + len(OTHER_SOURCES)

    # Phase 1: Blogs with Playwright
    print(f"\n[BLOGS] Парсинг блогов и гайдов ({len(BLOG_SOURCES)} источников)...")
    results = scrape_with_playwright(BLOG_SOURCES)
    all_results.extend(results)

    # Phase 2: GitHub sources
    print(f"\n[GITHUB] Парсинг GitHub ({len(GITHUB_SOURCES)} источников)...")
    results = scrape_github_raw(GITHUB_SOURCES)
    all_results.extend(results)

    # Phase 3: Reddit
    print(f"\n[REDDIT] Парсинг Reddit ({len(REDDIT_SOURCES)} источников)...")
    results = scrape_reddit(REDDIT_SOURCES)
    all_results.extend(results)

    # Phase 4: Other sources with Playwright
    print(f"\n[OTHER] Парсинг дополнительных источников ({len(OTHER_SOURCES)} источников)...")
    results = scrape_with_playwright(OTHER_SOURCES)
    all_results.extend(results)

    # Save sources.json
    SOURCES_JSON.write_text(json.dumps(all_results, indent=2, ensure_ascii=False), encoding="utf-8")

    # Summary
    ok_count = sum(1 for r in all_results if r["status"] == "OK")
    err_count = sum(1 for r in all_results if r["status"] == "ERROR")
    total_size = sum(r.get("size", 0) for r in all_results)

    print("\n" + "=" * 60)
    print("  === ОТЧЁТ ПАРСИНГА ===")
    print(f"  Собрано источников: {ok_count} из {len(all_results)}")
    print(f"  Не загрузилось: {err_count} (см. meta/errors.log)")
    print(f"  Общий размер данных: {total_size / 1024:.1f} KB")
    print(f"  Файлов создано: {len(list(RAW_DIR.glob('*.md')))}")
    print("=" * 60)


if __name__ == "__main__":
    main()
