from PIL import Image, ImageOps, ImageDraw
from pathlib import Path
src=Image.open('www/icon-512.png').convert('RGBA')
root=Path('android/app/src/main/res')
for density,size in [('mdpi',48),('hdpi',72),('xhdpi',96),('xxhdpi',144),('xxxhdpi',192)]:
    target=root/('mipmap-'+density);target.mkdir(parents=True,exist_ok=True)
    image=src.resize((size,size),Image.Resampling.LANCZOS)
    image.save(target/'ic_launcher.png')
    image.save(target/'ic_launcher_round.png')
    image.save(target/'ic_launcher_foreground.png')
# remove generated adaptive icon XML so launcher uses the exact Vrt image instead of Capacitor's default adaptive foreground
for f in (root/'mipmap-anydpi-v26').glob('ic_launcher*.xml'):
    f.unlink()
print('Vrt native launcher icons generated')
