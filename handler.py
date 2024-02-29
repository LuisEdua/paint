import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
import cv2

class Handler:
    def __init__(self, window):
        self.window = window
        self.canvas_width = 800
        self.canvas_height = 600
        self.canvas = tk.Canvas(window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.image = np.zeros((self.canvas_height, self.canvas_width, 3), dtype=np.uint8)
        self.image.fill(255)
        self.temp_image = self.image.copy()
        self.tools_window = tk.Toplevel(window)
        self.tools_window.title("Herramientas")
        self.tools_window.geometry("400x20")
        line_button = tk.Button(self.tools_window, text="Pen", command=lambda: self.select_tool(1))
        line_button.pack(side=tk.LEFT, fill=tk.Y, expand=True)
        polyline_button = tk.Button(self.tools_window, text="Linea", command=lambda: self.select_tool(2))
        polyline_button.pack(side=tk.LEFT, fill=tk.Y, expand=True)
        rectangle_button = tk.Button(self.tools_window, text="Rectángulo", command=lambda: self.select_tool(3))
        rectangle_button.pack(side=tk.LEFT, fill=tk.Y, expand=True)
        circle_button = tk.Button(self.tools_window, text="Círculo", command=lambda: self.select_tool(4))
        circle_button.pack(side=tk.LEFT, fill=tk.Y, expand=True)
        erase_button = tk.Button(self.tools_window, text="Borrar", command=lambda: self.select_tool(5))
        erase_button.pack(side=tk.LEFT, fill=tk.Y, expand=True)
        self.option = ""
        self.canvas.bind("<Button-1>", self.draw)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.draw)
        
    
    def select_tool(self, option):
        self.option = option
        
    def draw(self, event):
        x, y = event.x, event.y
        if event.type == "4":
            self.start = (x,y)
        if event.type == "6":
            self.temp_image = self.image.copy()
            if self.option == 1:
                cv2.line(self.temp_image, self.start, (x,y), (0,0,0), 1)
                cv2.line(self.image, self.start, (x,y), (0,0,0), 1)
                self.start = (x,y)
            if self.option == 2:
                cv2.line(self.temp_image, self.start, (x,y), (0,0,0), 1)
            if self.option == 3:
                cv2.rectangle(self.temp_image, self.start, (x,y), (0,0,0), 1)
            if self.option == 4:
                d = int(((self.start[0] - event.x)**2 + (self.start[1] - event.y)**2) ** 0.5)
                r = d // 2
                center_x = (self.start[0] + event.x) // 2
                center_y = (self.start[1] + event.y) // 2
                s = (center_x, center_y)
                cv2.circle(self.temp_image, s, r, (0,0,0), 1)
            if self.option == 5:
                cv2.line(self.temp_image, self.start, (x,y), (255,255,255), 20)
                cv2.line(self.image, self.start, (x,y), (255,255,255), 20)
                self.start = (x,y)
        if event.type == "5":
            if self.option == 1:
                cv2.line(self.temp_image, self.start, (x,y), (0,0,0), 1)
                cv2.line(self.image, self.start, (x,y), (0,0,0), 1)
                self.start = (x,y)
            if self.option == 2:
                cv2.line(self.temp_image, self.start, (x,y), (0,0,0), 1)
                cv2.line(self.image, self.start, (x,y), (0,0,0), 1)
            if self.option == 3:
                cv2.rectangle(self.temp_image, self.start, (x,y), (0,0,0), 1)
                cv2.rectangle(self.image, self.start, (x,y), (0,0,0), 1)
            if self.option == 4:
                d = int(((self.start[0] - event.x)**2 + (self.start[1] - event.y)**2) ** 0.5)
                r = d // 2
                center_x = (self.start[0] + event.x) // 2
                center_y = (self.start[1] + event.y) // 2
                s = (center_x, center_y)
                cv2.circle(self.image, s, r, (0,0,0), 1)
                cv2.circle(self.temp_image, s, r, (0,0,0), 1)
            if self.option == 5:
                cv2.line(self.temp_image, self.start, (x,y), (255,255,255), 20)
                cv2.line(self.image, self.start, (x,y), (255,255,255), 20)
        self.update_canvas()
        
    def update_canvas(self):
        self.photo = ImageTk.PhotoImage(image=Image.fromarray(self.temp_image))
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        