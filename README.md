# 🎂 Happy Birthday, Dii — Single-Page Gift Website

A custom, single-page birthday website built for **Dii** from her brother **Kabeer**.

---

## 📁 Project Directory
`/home/niraj/dii-birthday-website/`

> **Recommendation:** Set `/home/niraj/dii-birthday-website` as your active workspace in Antigravity for direct access and editing.

---

## 🌟 What's Included

1. **Gift Unwrapping Intro Screen**:
   - Opens like a wrapped gift with a wax seal stamp (`💌`) and interactive "Tap to Unwrap Your Gift" button.
   - Triggers an opening confetti explosion and gentle ambient chime.

2. **Hero Section with Birthday Lock & Countdown**:
   - Animated shimmer typography: *"Happy Birthday, Dii"*.
   - Subtitle: *"from a stranger on 16 Feb to my Dii"*.
   - **Scroll-Lock Active Before October 2**: Visitors are kept strictly on the hero page. Downstream content (Story Timeline, Gallery, Letter, Flip Cards, Promises, Final Surprise) is securely sealed and cannot be scrolled to.
   - Shows an elegant lock card: *"🔒 Gift Locked Until October 2 ⏳"*.
   - On **October 2** (or when toggling **"Preview Celebration Mode"**), the page unlocks with a confetti shower, celebration banner, and the scroll hint appears.


3. **Our Story Timeline**:
   - Vertical glowing timeline with 4 milestones:
     - **16 Feb**: Two strangers, no plans, no idea what was coming.
     - **Getting Close**: The unspoken comfort & late talks.
     - **The Sister's Shield**: *"Why don't you like my brother?"* — the moment the bond became unbreakable.
     - **Today & Forever**: Can't stay without each other, family by choice.

4. **Polaroid Scrapbook Photo Gallery with Lightbox**:
   - 6 polaroids with realistic paper tape, slight rotations, and handwritten captions.
   - Full-screen lightbox with smooth transition.
   - **Touch swipe support** (swipe left/right on phones) and keyboard navigation (Left/Right arrows, Escape).

5. **The Letter (The Emotional Centerpiece)**:
   - Paper-textured vintage card with deckled borders, wax stamp, and handwriting font (`Caveat`).
   - Exact text as provided, word-for-word, preserving all Urdu/Hindi sentiments (*Khuda na khasta*, *kabhi chhod ke mat jaana*).
   - Paragraph-by-paragraph scroll reveal as she scrolls down.
   - Pulsing heart next to your signature: `Your brother, Kabeer ❤️`.

6. **Why You're My Dii**:
   - Interactive 3D flip cards (touch friendly for phones, hover/click for desktop):
     1. Unspoken Understanding
     2. My Strength
     3. Safe Harbor
     4. Accepted
     5. Pure Happiness
     6. Family by Choice

7. **My Promises**:
   - Elegant rose-gold quote cards:
     - *"You will never face anything alone."*
     - *"I will always have time for you."*
     - *"Whatever you're going through, share it with this brother."*
     - *"Kabhi chhod ke mat jaana."*

8. **Final Surprise**:
   - "Tap to open your gift" button.
   - Triggers a grand multi-burst confetti shower and reveals the final message:
     **"Happy Birthday, Dii. Family by choice, forever. ❤️"**

9. **Extra Visual Polish & Sound**:
   - Canvas-based floating rose petals and golden stardust background.
   - Desktop cursor sparkle trail & mobile touch glow ripple.
   - Built-in soothing ambient music box lullaby (Web Audio API) that works 100% offline without needing an external audio file, plus support for an MP3 of your choice.

---

## 🛠️ How to Customize

### 1. Adding Your Real Photos
In `index.html`, around line 730 inside the `<script>` tag, look for `CONFIG.photos`:
```javascript
const CONFIG = {
  ...
  photos: [
    { src: "photo1.jpg", caption: "Where it all began — 16 February ☕✨" },
    { src: "photo2.jpg", caption: "The sweetest smile in the world 🌸" },
    ...
  ]
};
```
Just place your picture files in the same folder as `index.html` (e.g. `photo1.jpg`, `photo2.jpg`) and change the file names!

### 2. Adding Your Own Memory inside The Letter
Open `index.html` and search for:
`[PASTE YOUR OWN MEMORY HERE`

Replace that placeholder text with your favorite memory (e.g. a late-night talk or inside joke).

### 3. Music Configuration
- **The Grand Climax Track**: **`videoplayback.mp3`** ([`music/videoplayback.mp3`](file:///home/niraj/dii-birthday-website/music/videoplayback.mp3)) is reserved specifically for the grand finale! When Dii reaches Section 7 and taps **"Tap to open your gift"**, the confetti bursts, the card reveals *"Happy Birthday, Dii. Family by choice, forever. ❤️"*, and your song begins playing to celebrate the moment!
- **Optional Background Audio**: The floating audio button on the bottom right allows playing the fun track *"Hijabi Girl"* ([`music/hijabi-girl.mp3`](file:///home/niraj/dii-birthday-website/music/hijabi-girl.mp3)) or pausing anytime.





---

## 🚀 How to View Locally
Simply double-click `index.html` to open it in Chrome, Firefox, or Safari!

Or start a local web server:
```bash
cd /home/niraj/dii-birthday-website
python3 -m http.server 8080
```
Then visit `http://localhost:8080` on your computer or phone (via local WiFi IP).

---

## 🌐 How to Send It to Dii (Free Hosting)
To give Dii a link she can open on her phone:
- **Option A (GitHub Pages)**: Create a repository named `dii-birthday`, upload `index.html` (and your photos), then turn on GitHub Pages in repository settings.
- **Option B (Vercel / Netlify / Surge)**: Drag and drop the `dii-birthday-website` folder directly into [Netlify Drop](https://app.netlify.com/drop) or [Vercel](https://vercel.com) for a free instant URL.
