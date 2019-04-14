from tkinter import *
import numpy as np

class GridWorld(Frame):

  def __init__(self, master = None):
    self.master = master
    Frame.__init__(self, self.master)
    self.c = Canvas(self.master,  height=500, width=500, bg='black')
    self.sr = []
    self.init_zeros()
    self.create_grid()
    self.c.pack(fill = BOTH, expand=True)

  def create_grid(self):
    w = 500
    h = 500
    self.c.delete('grid_line')
    for i in range(0, 600, 100):
      self.c.create_line([(i, 0), (i, h)], tag='grid_line', fill = 'white')

    for i in range(0, 600, 100):
      self.c.create_line([(0, i), (w, i)], tag='grid_line', fill = 'white')

    # self.c.create_text(0 + 50, 0 + 10, text= 0.0, font="Verdana 8 bold", fill='white')
    # self.c.create_text(0 + 85, 0 + 50, text= 0.0, font="Verdana 8 bold", fill='white')
    # self.c.create_text(0 + 50, 0 + 90, text = 0.0, font="Verdana 8 bold", fill='white')
    # self.c.create_text(0 + 15, 0 + 50, text = 0.0, font="Verdana 8 bold", fill='white')

    j = 0
    y_coordinate = 0
    for i in range(0, w, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text = self.sr[j][1], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text = self.sr[j][2], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text = self.sr[j][3], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text = self.sr[j][4], font="Verdana 8 bold", fill='white')
      j += 1


    y_coordinate = 100
    for i in range(0, w, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text = self.sr[j][1], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text = self.sr[j][2], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text = self.sr[j][3], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text = self.sr[j][4], font="Verdana 8 bold", fill='white')
      j += 1

    y_coordinate = 200
    for i in range(0, w, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text = self.sr[j][1], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text = self.sr[j][2], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text = self.sr[j][3], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text = self.sr[j][4], font="Verdana 8 bold", fill='white')
      j += 1

    y_coordinate = 300
    for i in range(0, w, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text = self.sr[j][1], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text = self.sr[j][2], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text = self.sr[j][3], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text = self.sr[j][4], font="Verdana 8 bold", fill='white')
      j += 1

    y_coordinate = 400
    for i in range(0, w, 100):
      self.c.create_text(i + 50, y_coordinate + 10, text = self.sr[j][1], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 85, y_coordinate + 50, text = self.sr[j][2], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 50, y_coordinate + 90, text = self.sr[j][3], font="Verdana 8 bold", fill='white')
      self.c.create_text(i + 15, y_coordinate + 50, text = self.sr[j][4], font="Verdana 8 bold", fill='white')
      j += 1


  def init_zeros(self):
    s = 0
    x = 25
    y = 5

    self.sr = np.zeros([x, y], dtype=np.object)
    for x in range(25):
      self.sr[:, 1:] = float(0)
      self.sr[x][0] = s
      s = s + 1


class Main(GridWorld):
  def __init__(self):
    master = Tk()

    master.resizable(width = True, height = True)

    app = GridWorld(master)
    app.mainloop()

Main()
