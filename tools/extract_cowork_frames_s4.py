from __future__ import annotations

from pathlib import Path

import av
from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
VIDEO = ROOT / "Seance-4-Cowork.mp4"
OUT = ROOT / "img" / "session-04"


FRAMES: list[tuple[str, float, str]] = [
    ("01-download-claude-desktop.png", 286.0, "Page de téléchargement Claude Desktop"),
    ("03-cowork-home.png", 345.0, "Accueil Claude Cowork"),
    ("04-create-qg-folder.png", 364.0, "Création du dossier QG"),
    ("05-choose-folder-menu.png", 372.0, "Choisir un autre dossier"),
    ("06-finder-qg-denem.png", 377.0, "Fenêtre Finder du QG"),
    ("07-connectors-menu.png", 489.0, "Menu des connecteurs"),
    ("08-connectors-directory.png", 509.0, "Répertoire des connecteurs"),
    ("09-settings-connectors.png", 585.0, "Paramètres et connecteurs"),
    ("10-custom-mcp-connector.png", 606.0, "Connecteur personnalisé MCP"),
    ("11-google-calendar-detail.png", 639.0, "Détail Google Calendar"),
    ("12-connected-tools-menu.png", 708.0, "Connecteurs actifs dans Cowork"),
    ("13-calendar-task-auth.png", 720.0, "Lancement de la tâche Calendar"),
    ("14-calendar-progress.png", 765.0, "Progression de création des événements"),
    ("15-final-menu-connectors.png", 822.0, "Résultat et menu connecteurs"),
    ("16-skills-directory.png", 1289.0, "Répertoire des compétences"),
]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except Exception:
            pass
    return ImageFont.load_default()


def save_spotlight_image(target: Path) -> None:
    image = Image.new("RGB", (1920, 1080), "#edf7fb")
    bg = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(bg)
    for x in range(0, 1920, 80):
        color = (226, 242, 248, 110) if x % 160 == 0 else (245, 250, 252, 160)
        draw.rectangle([x, 0, x + 80, 1080], fill=color)
    bg = bg.filter(ImageFilter.GaussianBlur(42))
    image = Image.alpha_composite(image.convert("RGBA"), bg)

    panel = Image.new("RGBA", (1500, 780), (255, 255, 255, 218))
    panel = panel.filter(ImageFilter.GaussianBlur(0.4))
    shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle([150, 85, 1650, 865], radius=38, fill=(15, 23, 42, 55))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    image = Image.alpha_composite(image, shadow)
    image.alpha_composite(panel, (150, 85))

    d = ImageDraw.Draw(image)
    d.text((205, 135), "CLA", fill="#111827", font=font(62, True))
    d.line((185, 230, 1615, 230), fill=(209, 213, 219, 220), width=3)
    d.rounded_rectangle((180, 260, 1600, 355), radius=18, fill=(238, 235, 233, 235))
    d.rounded_rectangle((205, 280, 260, 335), radius=14, fill="#ef6f4d")
    d.text((220, 287), "✳", fill="white", font=font(34, True))
    d.text((300, 288), "Claude", fill="#1f2937", font=font(36, False))
    d.text((1280, 297), "Rechercher dans Claude", fill="#9ca3af", font=font(24, False))
    d.rounded_rectangle((1500, 287, 1590, 329), radius=12, fill=(255, 255, 255, 235))
    d.text((1515, 296), "tabulation", fill="#9ca3af", font=font(20, True))
    d.rounded_rectangle((205, 395, 260, 450), radius=10, fill="#e5eef3")
    d.text((300, 408), "Claude Code URL Handler", fill="#1f2937", font=font(34, False))
    d.text((184, 122), "⌘", fill="#6b7280", font=font(46, False))
    image.convert("RGB").save(target)


def save_frame(container: av.container.InputContainer, timestamp: float, target: Path) -> None:
    stream = container.streams.video[0]
    container.seek(int(timestamp / stream.time_base), any_frame=False, backward=True, stream=stream)
    selected = None
    for frame in container.decode(stream):
        if frame.time is not None and frame.time >= timestamp:
            selected = frame
            break
    if selected is None:
        raise RuntimeError(f"No frame found at {timestamp}")
    image = selected.to_image()
    image.save(target)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    save_spotlight_image(OUT / "02-open-claude-app.png")
    with av.open(str(VIDEO)) as container:
        for filename, timestamp, _label in FRAMES:
            save_frame(container, timestamp, OUT / filename)
    print(f"Extracted {len(FRAMES) + 1} images to {OUT}")


if __name__ == "__main__":
    main()
