
from PIL import Image
import os

def images_to_pdf(image_folder, output_pdf):
    # قراءة جميع الصور في المجلد وترتيبها
    images = []
    for file_name in sorted(os.listdir(image_folder)):
        if file_name.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, file_name)
            img = Image.open(image_path).convert('RGB')
            images.append(img)
    
    if images:
        # حفظ الصور في ملف PDF واحد
        images[0].save(output_pdf, save_all=True, append_images=images[1:])
        print(f"✅ تم إنشاء ملف PDF بنجاح: {output_pdf}")
    else:
        print("⚠️ لم يتم العثور على صور في المجلد المحدد.")

if __name__ == "__main__":
    # مسار المجلد + اسم ملف PDF الناتج
    folder_path = input("📁 أدخل مسار مجلد الصور: ")
    output_file = input("📄 أدخل اسم ملف PDF الناتج (مثلاً output.pdf): ")
    
    images_to_pdf(folder_path, output_file)
