from PIL import Image
import numpy as np
import os


def enhance_contrast(image_path, output_path=None):
    try:

        img = Image.open(image_path).convert('L')
        data = np.array(img)


        min_val = np.min(data)
        max_val = np.max(data)

        if min_val == max_val:
            print("Ошибка: Все пиксели одинаковые")
            return


        enhanced_data = ((data - min_val) / (max_val - min_val) * 255).astype(np.uint8)

        if output_path is None:
            base = os.path.splitext(image_path)[0]
            ext = os.path.splitext(image_path)[1]
            output_path = f"{base}_enhanced{ext}"

        Image.fromarray(enhanced_data).save(output_path)
        print(f"Сохранено: {output_path}")

    except Exception as e:
        print(f"Ошибка: {e}")

enhance_contrast("lunar02_raw.jpg")
enhance_contrast("lunar03_raw.jpg")
