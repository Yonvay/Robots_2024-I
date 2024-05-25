from tkinter import Tk, ttk, Frame, Label, Button, Radiobutton, StringVar, LEFT
from PIL import ImageTk, Image
from pathlib import Path

# Get the current working directory
current_dir = Path.cwd()

def show_encabezado(root):
    global current_dir
    frm_encabezado = Frame(root, bg="#cccccc")
    frm_encabezado.pack(fill='x')

    img_logo = Image.open(current_dir / "IMGS" / "LogotipoUnal.svg")
    img_logo = img_logo.resize((100, 100), Image.LANCZOS)  # resize to 100x100 pixels
    img_logo = ImageTk.PhotoImage(img_logo)  # convert the image object to a tkinter-compatible photo image
    img_pose_label = Label(frm_encabezado, image=img_logo)
    img_pose_label.image = img_logo  # keep a reference to the image to prevent it from being garbage collected
    img_pose_label.pack(side=LEFT)

    frm_names = Frame(frm_encabezado, bg="#94b43b")
    frm_names.pack(side=LEFT, fill='both', expand=True)

    # Create three labels under each other
    lb_lab4 = Label(frm_names, text="Laboratorio 4, Cinemática Directa - Phantom X - ROS", bg="#94b43b")
    lb_lab4.pack(fill='x')

    lb_name1= Label(frm_names, text="Maria Alejandra Peréz Petro", bg="#94b43b")
    lb_name1.pack(fill='x')

    lb_name2 = Label(frm_names, text="Yovany Esneider Vargas Gutierrez", bg="#94b43b")
    lb_name2.pack(fill='x')

    Button(frm_encabezado, text="Quit", command=root.destroy).pack(side=LEFT)

    
# Function that displays an image based on the selected radio button
def get_selected_radiobutton(radio_var, img_pose_label):
    global current_dir
    # Get the selected radio button
    selected_option = radio_var.get()
    #print(selected_option)

    # Map the selected option to an image file
    img_file = {
        "Pose 1": current_dir / "IMGS" / "pose1.png",
        "Pose 2": current_dir / "IMGS" / "pose2.png",
        "Pose 3": current_dir / "IMGS" / "pose3.png",
        "Pose 4": current_dir / "IMGS" / "pose4.png",
        "Pose 5": current_dir / "IMGS" / "pose5.png",
    }.get(selected_option, current_dir / "IMGS" / "default.jpg")

    # Load the image
    img = Image.open(img_file)

    # Convert the image to a PhotoImage object
    photo = ImageTk.PhotoImage(img)

    # Set the image of the label
    img_pose_label.config(image=photo)
    img_pose_label.image = photo  # Keep a reference to the image to prevent it from being garbage collected


def show_radio_buttons(root):
    # Create a frame to hold the radio buttons
    frm_radio = Frame(root)
    frm_radio.pack()

    # Create a label to display the image
    img_pose_label = Label(root)
    img_pose_label.pack()

    # Create a variable to keep track of which radio button is selected
    radio_var = StringVar()
    radio_var.set(None)  # Set the default value to an empty string

    # Create five radio buttons
    for i in range(5):
        rb = Radiobutton(frm_radio, text=f"Pose {i+1}", variable=radio_var, value=f"Pose {i+1}", 
                     command=lambda: get_selected_radiobutton(radio_var, img_pose_label))
        rb.pack(side=LEFT)

def main():

    root = Tk() # Create an instance of tkinter window
    root.geometry("800x600") # Define the geometry of the window
    root.title("HMI") # Set the title of the window

    show_encabezado(root)

    show_radio_buttons(root)

    root.mainloop()

if __name__ == "__main__":
    main()
