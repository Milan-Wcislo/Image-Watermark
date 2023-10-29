from PIL import Image, ImageTk
from tkinter import Tk, Label, filedialog, Button, messagebox

def browse_image():
    global combined_image, file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        try:
            main_image = Image.open(file_path)
            watermark_image = Image.open("Milan-logos_transparent.png")
            resized_watermark = watermark_image.resize((int(watermark_image.width * 0.1), int(watermark_image.width * 0.1)))

            position = (main_image.width - resized_watermark.width, main_image.height - resized_watermark.height)
            
            combined_image = Image.new("RGB", main_image.size)
            combined_image.paste(main_image, (0, 0))
            combined_image.paste(resized_watermark, position, mask=resized_watermark)
            
            # combined_image.save(file_path)

            photo = ImageTk.PhotoImage(combined_image)

            image_label.config(image=photo)
            image_label.image = photo

        except Exception as e:
            print(f"Error opening image: {e}")

def save_image():
    try:
        combined_image.save(file_path)
        messagebox.showinfo("Success", "Image saved successfully!")
    except NameError:
        messagebox.showerror("Error", "Please open an image first!")

root = Tk()
root.title("Image Watermark")
root.geometry("400x400")
root.config(padx=40, pady=40)

# Create a button to open the file browser
browse_button = Button(root, text="Browse", command=browse_image, bg="#222", fg="white", font=("Arial", 16), highlightthickness=0)
browse_button.grid(column=0, row=0, padx=10, pady=10)

save_button = Button(root, text="Save", command=save_image, bg="#222", fg="white", font=("Arial", 16), highlightthickness=0)
save_button.grid(column=1, row=0, padx=10, pady=10)

# Create a label to display the image
image_label = Label(root)
image_label.grid(column=0, row=1, padx=10, pady=10, columnspan=2)

root.mainloop()
