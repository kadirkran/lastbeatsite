"""Generates index.html, support.html and privacy.html (shared header/footer).
Edit the constants below, then run:  python build_site.py
"""
import os

APP = "Last Beat"
DEVELOPER = "Coacta Lab"
CONTACT_EMAIL = "contact@coactalab.com"
UPDATED = "October 2, 2026"
SITE_BASE = "https://kadirkran.github.io/lastbeatsite"

HERE = os.path.dirname(os.path.abspath(__file__))


def page(filename, title, desc, body, current):
    nav = ""
    for href, label in (("index.html", "Home"), ("support.html", "Support"), ("privacy.html", "Privacy")):
        cur = ' aria-current="page"' if href == current else ""
        nav += f'<a href="{href}"{cur}>{label}</a>'
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#101a17">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{SITE_BASE}/assets/icon-512.png">
<link rel="icon" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">
<header class="site">
  <a class="brand" href="index.html"><img src="assets/favicon.png" alt="">{APP}</a>
  <nav>{nav}</nav>
</header>
{body}
<footer class="site">
  <span>&copy; 2026 {DEVELOPER}. All rights reserved.</span>
  <span><a href="support.html">Support</a> &middot; <a href="privacy.html">Privacy Policy</a> &middot; <a href="mailto:{CONTACT_EMAIL}">Contact</a></span>
</footer>
</div>
</body>
</html>
"""
    with open(os.path.join(HERE, filename), "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


# ---------------------------------------------------------------- marketing
index_body = f"""
<main>
  <section class="hero">
    <img class="icon" src="assets/icon-512.png" alt="{APP} app icon">
    <h1>{APP}</h1>
    <div class="tag">One tap. Perfect timing.</div>
    <p class="lead">A calm, fast reflex game. Your ball never stops &mdash; rotate the tile one step ahead
    at exactly the right moment and keep the lane connected for as long as you can.</p>
    <div class="badges">
      <span class="badge soon">App Store &mdash; coming soon</span>
      <span class="badge soon">Google Play &mdash; coming soon</span>
    </div>
  </section>

  <section class="grid" aria-label="Features">
    <div class="card"><h3>ONE-TAP CONTROL</h3><p>Tap to rotate the glowing tile before the ball arrives. Easy to learn, hard to master.</p></div>
    <div class="card"><h3>PERFECT TIMING</h3><p>Turn at the last moment for a PERFECT, build a combo, and trigger FEVER for 4&times; points.</p></div>
    <div class="card"><h3>NEW TILES</h3><p>Marble, glitch, fragile, gate, drifter and boost tiles keep every run fresh.</p></div>
    <div class="card"><h3>DAILY CHALLENGE</h3><p>One shared path every day, daily quests, a streak bonus and a lucky spin.</p></div>
    <div class="card"><h3>CALM LOOK</h3><p>Soft sage tiles, a night-forest backdrop and a gentle light-ribbon trail. Made to relax.</p></div>
    <div class="card"><h3>13 LANGUAGES</h3><p>English, T&uuml;rk&ccedil;e, Deutsch, Espa&ntilde;ol, Fran&ccedil;ais, Italiano, Portugu&ecirc;s, &#1056;&#1091;&#1089;&#1089;&#1082;&#1080;&#1081;, &#1593;&#1585;&#1576;&#1610;, &#26085;&#26412;&#35486;, &#54620;&#44397;&#50612;, &#31616;&#20307;&#20013;&#25991; and Kurd&icirc;.</p></div>
  </section>
</main>
"""
page("index.html", f"{APP} - One tap. Perfect timing.",
     "Last Beat is a calm one-tap reflex game: rotate the tile ahead at the perfect moment and keep the ball rolling.",
     index_body, "index.html")

# ------------------------------------------------------------------ support
support_body = f"""
<main class="doc">
  <h1>Support</h1>
  <div class="meta">{APP} &middot; Help &amp; contact</div>

  <div class="contact">
    <strong>Need a hand?</strong> Email us at
    <a href="mailto:{CONTACT_EMAIL}?subject={APP}%20support">{CONTACT_EMAIL}</a>.
    Please include your device model, OS version and a short description of the problem
    (a screenshot helps). We usually reply within 2&ndash;3 business days.
  </div>

  <h2>Frequently asked questions</h2>
  <div class="faq">
    <details><summary>How do I play?</summary>
      <p>Your ball rolls forward by itself. Tap the screen to rotate the glowing tile one step ahead (90&deg; clockwise)
      until its groove connects the path. Tap at the very last moment before the ball arrives for a PERFECT (+3 points).
      The first run includes a short guided tutorial; replay it any time with <strong>How to play</strong> in the main menu.</p></details>
    <details><summary>What are FEVER, PERFECT and combos?</summary>
      <p>Six PERFECT turns in a row start FEVER for 3 seconds: tiles align automatically and every tile is worth 4&times; points.</p></details>
    <details><summary>What do the special tiles do?</summary>
      <p><strong>Marble</strong> needs two taps (the first unlocks it). <strong>Glitch</strong> rotates the other way.
      <strong>Fragile</strong> collapses after you pass. <strong>Gate</strong> accepts exactly one tap.
      <strong>Drifter</strong> turns by itself until the last moment. <strong>Boost</strong> gives a short speed burst.</p></details>
    <details><summary>What are gems for?</summary>
      <p>Gems unlock ball skins in <strong>Balls</strong>. You earn them from runs, daily quests, your streak, the daily spin and the free gift.</p></details>
    <details><summary>How do the ads work?</summary>
      <p>Ads are optional where you get a reward: watch an ad to continue after a game over, double your gems, spin once more,
      take the free gift, or try a locked ball for one run. A short full-screen ad may also appear after every third finished game.</p></details>
    <details><summary>My ad did not give me the reward.</summary>
      <p>Make sure you watched the ad until the end and tapped the claim/close button. If it still failed, email us with the date, time and what you were trying to unlock.</p></details>
    <details><summary>How do I change the language?</summary>
      <p>Tap the globe icon at the top of the main menu. The game starts in English until you choose another language.</p></details>
    <details><summary>The sound or music is missing.</summary>
      <p>Check that sound is on (speaker icon in the main menu or pause screen) and that your device is not in silent mode.
      Music plays only in the main menu.</p></details>
    <details><summary>Will I lose my progress if I reinstall or change phones?</summary>
      <p>Progress (best score, gems, balls, quests) is stored only on your device, so it is removed when you uninstall the app and is not transferred automatically to a new device.</p></details>
    <details><summary>The game is slow or stutters.</summary>
      <p>Last Beat lowers its visual effects automatically when it detects slow frames. Closing other apps and restarting the game usually helps.
      If it persists, email us your device model.</p></details>
    <details><summary>How do I delete my data?</summary>
      <p>We do not keep an account or server-side profile for you. Uninstalling the app deletes everything stored on your device.
      See the <a href="privacy.html">Privacy Policy</a> for details on advertising data.</p></details>
  </div>
</main>
"""
page("support.html", f"{APP} Support",
     "Help, FAQ and contact for the Last Beat game.", support_body, "support.html")

# ------------------------------------------------------------------ privacy
privacy_body = f"""
<main class="doc">
  <h1>Privacy Policy</h1>
  <div class="meta">{APP} &middot; Last updated: {UPDATED}</div>

  <p>This policy explains what information the <strong>{APP}</strong> mobile game (&ldquo;the app&rdquo;) uses,
  and the choices you have. The app is published by <strong>{DEVELOPER}</strong> (&ldquo;we&rdquo;, &ldquo;us&rdquo;).
  Questions: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>.</p>

  <h2>1. Summary</h2>
  <ul>
    <li>No account, no sign-in, and we do not ask for your name, email, location, contacts, photos or microphone.</li>
    <li>Your game progress stays on your device.</li>
    <li>The app shows ads provided by a third-party advertising network, which may collect certain device information as described below.</li>
  </ul>

  <h2>2. Information stored on your device</h2>
  <p>To let you continue where you left off, the app saves the following on your device only (it is not sent to us):
  best score, gems and unlocked balls, selected ball, quest and streak progress, daily challenge and daily spin status,
  your language and sound settings, and whether you have finished the tutorial. Uninstalling the app deletes this data.</p>

  <h2>3. Information we collect</h2>
  <p>We do not operate a server that receives your gameplay data, and we do not currently use our own analytics or crash-reporting tools.
  We do not knowingly collect personal information directly from you.</p>

  <h2>4. Advertising</h2>
  <p>The app displays rewarded ads (which you can choose to watch for a benefit) and occasional full-screen ads.
  These ads are delivered by a third-party advertising network (for example Google AdMob).
  To serve, measure and limit the frequency of ads and to prevent fraud, the ad provider may collect and use
  information such as your device&rsquo;s advertising identifier, IP address, device and OS information,
  app interaction data and approximate location derived from the IP address. Depending on your region and settings,
  ads may be personalised.</p>
  <ul>
    <li>Where required (for example in the European Economic Area and the UK), we ask for your consent before personalised ads are shown, and you can change your choice at any time in the app or your device settings.</li>
    <li><strong>iOS:</strong> if the app asks to track you across apps and websites, you can allow or deny this; you can also change it in Settings &gt; Privacy &amp; Security &gt; Tracking.</li>
    <li><strong>Android:</strong> you can reset or delete your advertising ID and opt out of ads personalisation in Settings &gt; Google &gt; Ads.</li>
  </ul>
  <p>The ad provider&rsquo;s own privacy policy applies to the data it collects, for example
  <a href="https://policies.google.com/privacy">policies.google.com/privacy</a> and
  <a href="https://policies.google.com/technologies/partner-sites">how Google uses information from sites or apps that use its services</a>.</p>

  <h2>5. Sharing your score</h2>
  <p>If you tap <strong>Share</strong> after a game, your device&rsquo;s share sheet opens with a short text containing your score.
  You choose the app and recipient; we do not receive this information.</p>

  <h2>6. Purchases</h2>
  <p>The app has no real-money purchases at this time. Gems are an in-game currency earned by playing and cannot be bought.
  If this changes, purchases will be processed by Apple or Google and this policy will be updated.</p>

  <h2>7. Children</h2>
  <p>The app is not directed to children under 13 (or the minimum age required in your country), and we do not knowingly collect personal information from children.
  If you believe a child has provided personal information, contact us and we will help.</p>

  <h2>8. Data retention and your rights</h2>
  <p>Because we do not hold your personal data on our servers, there is nothing for us to export or delete; removing the app clears the data stored on your device.
  Depending on where you live (for example under the GDPR, UK GDPR or CCPA/CPRA) you may have rights regarding data processed by our advertising partner,
  such as access, deletion, objection to personalised advertising, or withdrawing consent. You can exercise these through the ad provider&rsquo;s tools or by contacting us at the address above.</p>

  <h2>9. Security</h2>
  <p>We keep stored data on your device and use reputable third-party providers for advertising. No method of electronic storage or transmission is 100% secure.</p>

  <h2>10. International transfers</h2>
  <p>Our advertising partner may process data in countries other than your own, subject to the safeguards described in the partner&rsquo;s policy.</p>

  <h2>11. Changes to this policy</h2>
  <p>We may update this policy from time to time. The &ldquo;Last updated&rdquo; date above shows the latest version, and material changes will be reflected in the app or on this page.</p>

  <h2>12. Contact</h2>
  <p>{DEVELOPER}<br><a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></p>
</main>
"""
page("privacy.html", f"{APP} Privacy Policy",
     "How Last Beat handles data: on-device progress and third-party advertising.", privacy_body, "privacy.html")
print("site generated")
