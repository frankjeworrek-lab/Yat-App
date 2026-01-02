from PIL import Image
import sys
import os

def create_iconset(source_path, output_dir, zoom=1.0):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    sizes = [16, 32, 64, 128, 256, 512]
    
    try:
        img = Image.open(source_path)
    except Exception as e:
        print(f"❌ Error opening image {source_path}: {e}")
        sys.exit(1)
    
    # Ensure RGBA
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
        
    print(f"ℹ️  Source size: {img.size}")
    
    # Apply Zoom / Crop
    if zoom > 1.0:
        print(f"🔍 Applying Zoom: {zoom}x")
        w, h = img.size
        # Calculate crop box (keep center)
        # New dimension = Old / Zoom
        new_w = w / zoom
        new_h = h / zoom
        
        left = (w - new_w) / 2
        top = (h - new_h) / 2
        right = (w + new_w) / 2
        bottom = (h + new_h) / 2
        
        img = img.crop((left, top, right, bottom))
        print(f"   New size after crop: {img.size}")

    for size in sizes:
        out_name = f"icon_{size}x{size}.png"
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(os.path.join(output_dir, out_name))
        
        out_name_2x = f"icon_{size}x{size}@2x.png"
        double_size = size * 2
        if double_size <= 1024:
            resized_2x = img.resize((double_size, double_size), Image.Resampling.LANCZOS)
            resized_2x.save(os.path.join(output_dir, out_name_2x))
            
    print(f"✅ Generated iconset in {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 icon_gen.py <source.png> <output_dir> [zoom_factor]")
        sys.exit(1)
    
    src = sys.argv[1]
    dst = sys.argv[2]
    zoom_factor = 1.0
    
    if len(sys.argv) > 3:
        try:
            zoom_factor = float(sys.argv[3])
        except ValueError:
            print("Warning: Invalid zoom factor, using 1.0")
            
    create_iconset(src, dst, zoom=zoom_factor)
