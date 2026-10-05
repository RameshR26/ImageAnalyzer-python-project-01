import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import os


# Create output folder
os.makedirs("output", exist_ok=True)

# Global variable for image
image = None


def read_image():
    global image

    image = cv2.imread("input.jpg")

    if image is None:
        print("Error: Image not found!")
        return

    print("\nImage loaded successfully!")


def display_properties():
    if image is None:
        print("Please read the image first.")
        return

    height, width, channels = image.shape

    print("\n================================")
    print("       IMAGE PROPERTIES")
    print("================================")
    print("Width      :", width)
    print("Height     :", height)
    print("Channels   :", channels)
    print("Data Type  :", image.dtype)


def display_image():
    if image is None:
        print("Please read the image first.")
        return

    cv2.imshow("Original Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def crop_image():
    if image is None:
        print("Please read the image first.")
        return

    height, width = image.shape[:2]

    # Crop center portion
    x1 = width // 4
    y1 = height // 4
    x2 = 3 * width // 4
    y2 = 3 * height // 4

    cropped = image[y1:y2, x1:x2]

    cv2.imwrite("output/cropped.jpg", cropped)

    print("Cropped image saved as output/cropped.jpg")

    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize_image():
    if image is None:
        print("Please read the image first.")
        return

    resized = cv2.resize(image, (500, 500))

    cv2.imwrite("output/resized.jpg", resized)

    print("Resized image saved as output/resized.jpg")

    cv2.imshow("Resized Image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def grayscale_image():
    if image is None:
        print("Please read the image first.")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("output/grayscale.jpg", gray)

    print("Grayscale image saved as output/grayscale.jpg")

    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_image_details():
    if image is None:
        print("Please read the image first.")
        return

    height, width, channels = image.shape

    details = {
        "filename": "input.jpg",
        "width": width,
        "height": height,
        "channels": channels,
        "data_type": str(image.dtype)
    }

    with open("output/image_details.json", "w") as file:
        json.dump(details, file, indent=4)

    print("Image details saved in output/image_details.json")


def view_image_data():
    try:
        with open("output/image_details.json", "r") as file:
            data = json.load(file)

        df = pd.DataFrame([data])

        print("\n================================")
        print("       IMAGE DATA")
        print("================================")

        print(df)

    except FileNotFoundError:
        print("Please save image details first.")


def generate_graph():
    if image is None:
        print("Please read the image first.")
        return

    height, width = image.shape[:2]

    labels = ["Width", "Height"]
    values = [width, height]

    plt.bar(labels, values)

    plt.title("Image Dimensions")
    plt.xlabel("Property")
    plt.ylabel("Pixels")

    plt.savefig("output/image_graph.png")

    plt.show()

    print("Graph saved as output/image_graph.png")


def main():

    while True:

        print("\n================================")
        print("          IMAGE ANALYZER")
        print("================================")

        print("1. Read Image")
        print("2. Display Image")
        print("3. Display Image Properties")
        print("4. Crop Image")
        print("5. Resize Image")
        print("6. Convert to Grayscale")
        print("7. Save Image Details")
        print("8. View Image Data")
        print("9. Generate Graph")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            read_image()

        elif choice == "2":
            display_image()

        elif choice == "3":
            display_properties()

        elif choice == "4":
            crop_image()

        elif choice == "5":
            resize_image()

        elif choice == "6":
            grayscale_image()

        elif choice == "7":
            save_image_details()

        elif choice == "8":
            view_image_data()

        elif choice == "9":
            generate_graph()

        elif choice == "10":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()