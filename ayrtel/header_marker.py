import cv2
import json

header_boxes = []
drawing = False
start_point = (0, 0)
frame_copy = None


def draw_rectangle(event, x, y, flags, param):
    global start_point, drawing, frame_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        img_temp = frame_copy.copy()
        cv2.rectangle(img_temp, start_point, (x, y), (0, 255, 0), 1)
        cv2.imshow("Select Headers", img_temp)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv2.rectangle(frame_copy, start_point, end_point, (0, 255, 0), 2)
        header_boxes.append((start_point, end_point))
        idx = len(header_boxes)
        cv2.putText(
            frame_copy,
            f"H{idx}",
            start_point,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )
        cv2.imshow("Select Headers", frame_copy)


def select_headers_from_frame(image_path):
    global frame_copy
    frame = cv2.imread(image_path)
    frame_copy = frame.copy()

    cv2.namedWindow("Select Headers")
    cv2.setMouseCallback("Select Headers", draw_rectangle)
    cv2.imshow("Select Headers", frame_copy)

    print(
        "Draw rectangles for headers. Press 's' to save and exit, or 'q' to quit without saving."
    )
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord("s"):
            with open("header_boxes.json", "w") as f:
                json.dump(header_boxes, f)
            print("Saved header boxes.")
            break
        elif key == ord("q"):
            print("Exiting without saving.")
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    select_headers_from_frame("data/frame_header_mark.png")
