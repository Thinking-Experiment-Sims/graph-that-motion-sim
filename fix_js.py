with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

clean_praise = '''        const cocoSuccessPraise = [
            "🐾 Pawsome job! You nailed the slope! Here\\'s a virtual treat! 🦴",
            "🐾 Woof! That\\'s a treat-worthy match! Coco approved! 🎾",
            "🐾 Tail-wagging brilliance! You translated my zoomies into math! ⭐",
            "🐾 Spot on! You know your velocity from your position! 🐶",
            "🐾 Bark-tastic! You decoded my run like a physics champion! 🥓",
            "🐾 High four! You\\'re a certified Kinematics Master! 🐾"
        ];

        const cocoErrorQuotes = [
            "🐾 Ruh-roh! Barking up the wrong graph! Let\\'s paws and try again...",
            "🐾 Sniffing in the wrong direction! Replay my run and watch my pawprints! 🦴",
            "🐾 Paws and reflect! Look closely at whether that\\'s a Position or Velocity graph! 🐶",
            "🐾 Not quite! My tail says check if I was speeding up or slowing down! 🐕",
            "🐾 Hold your leash! Double-check the direction of my trot! 🐾"
        ];'''

html = re.sub(r'const cocoSuccessPraise = \[[\s\S]*?const cocoErrorQuotes = \[[\s\S]*?\];', clean_praise, html)

with open('/Users/vladimir.lopez/Library/CloudStorage/GoogleDrive-vladimir.lopez@kinkaid.org/My Drive/AI/AI Workspace/motion_simulation/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Replacement complete.")
