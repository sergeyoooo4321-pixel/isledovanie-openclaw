# Reddit r/openclawpirates — Top All Time
**URL:** https://www.reddit.com/r/openclawpirates/top/?t=all  
**Дата сбора:** 2026-04-05 21:05  
**Статус:** OK  

---

ИСТОЧНИК 5: r/openclawpirates — Top All Time

URL: https://www.reddit.com/r/openclawpirates/top/?t=all

Статус: OK (малоактивный сабреддит)

Описание: OpenClaw Pirates - share only things that might get your fired. Created Jan 31, 2026. 682 weekly visitors.
POST 1

Заголовок: I built a system to completely replace myself at work using OpenClaw.

Author: u/basiclaser | Score: 49 | Flair: -

Permalink: r/openclawpirates (27 days ago)





Текст: [Только заголовок, текст поста не раскрыт в скрапе]





----------------------------------------------------------------





POST 2

Заголовок: How to vet OpenClaw skills so you don't install malware by accident

Author: u/missjesstin | Score: 9 | Flair: -

Permalink: r/openclawpirates (2 months ago)





Текст:

OpenClaw skills are just code with a nice name. Installing a skill without checking it is basically running a random script you found on the internet, except now it has an AI deciding when to execute it.





First rule: if you cannot see the code, do not install it. Period.





Check for obvious red flags by searching repo for: curl, wget, fetch, os.system, subprocess, exec, eval, base64. Not automatically bad, but where bad things usually hide.





Check network behavior: if it's a local file organizer, it should not be talking to external servers.





Look closely at configuration files and environment variables: normal skill needs one API key; sketchy one asks for everything, or silently reads from all env vars.





Check file access scope: safe skill works inside clearly defined directory. Dangerous one uses relative paths, home directory access, or recursive scans.





Watch what skill does with outputs: if it prints or stores large blobs "for debugging", that data can leak later.





Look for persistence: see if skill writes files outside its function (startup scripts, hidden files, background processes).





Run it in isolation first: new VM, container, or locked-down test agent. Give it fake data. Fake API keys.





Check commit history: One commit, no discussion, random username, recent repo — higher risk.





Final rule: skills should be boring. The more "powerful" and magical a skill sounds, the more dangerous it usually is.





----------------------------------------------------------------





POST 3

Заголовок: How an OpenClaw agent, Larry, got millions of TikTok views in one week. (Full step-by-step guide)

Author: u/missjesstin | Score: 6 | Flair: -

Permalink: r/openclawpirates (2 months ago)





Текст:

Written by Oliver Henry and Larry. Larry is an agent running on an old gaming PC under the desk.





Larry's tools:

- Access to read and write files on machine

- Ability to generate images through OpenAI's API (gpt-image-1.5)

- Code he writes himself to add text overlays

- Access to post to TikTok via social media scheduling API

- Skill files that teach him specific workflows

- Memory files where he logs every lesson learned

- Control via WhatsApp





Apps being promoted: Snugly (AI room makeover) and Liply (AI lip filler preview).





TikTok format: photo carousels (slideshows get 2.9x more comments, 1.9x more likes, 2.6x more shares vs video per TikTok's own data). 6 slides exactly. Text overlay on slide 1 with hook.





Image generation with gpt-image-1.5: "lock the architecture" — one incredibly detailed room description copy-pasted into every single prompt. Only the style changes between slides.





Example prompt structure: [Locked architecture: room dimensions, window count and position, door location, camera angle, furniture size, ceiling height, floor type] + [Only changing: style, wall color, bedding, decor, lighting]





Posting workflow: Larry generates images → adds text overlays → writes caption → uploads to TikTok as draft (privacy_level: "SELF_ONLY") → Oliver opens TikTok, picks trending sound, pastes caption, hits publish. Oliver's part: ~60 seconds.





Hooks that FAILED (200-900 views):

- "Why does my flat look like a student loan" → 905 views

- "See your room in 12+ styles before you commit" → 879 views





Hooks that WORKED (100K+ views):

- "My landlord said I can't change anything so I showed her what AI thinks it could look like" → 234,000 views

- "I showed my mum what AI thinks our living room could be" → 167,000 views

- "My landlord wouldn't let me decorate until I showed her these" → 147,000 views





Formula: [Another person] + [conflict or doubt] → showed them AI → they changed their mind





Results (under 1 week): 500K+ total TikTok views, 234K views on top post, 4 posts over 100K views, 108 paying subscribers, ~$588/month MRR. Cost per post: ~$0.50 in API calls.





Larry's skill file is over 500 lines long. Every failure became a rule. Every success became a formula. He compounds.
