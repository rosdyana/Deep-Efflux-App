# /**
#  * @author [Rosdyana Kusuma]
#  * @email [rosdyana.kusuma@gmail.com]
#  * @create date 2018-05-09 12:20:39
#  * @modify date 2018-05-09 12:20:39
#  * @desc [Deep Efflux App based on Python]
# */

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
import sys

PROGNAME = 'Deep Efflux'
VERSION = "0.1"
fields = 'Name', 'Length', 'Family A', 'Family B', 'Family C'


class Application(tk.Frame):
    def __init__(self, master=None, filename=None):

        tk.Frame.__init__(self, master)
        self.grid()
        self.createMenuBar()
        self.makeform(self, fields)
        if not(filename):
            filenames = filedialog.askopenfilenames(master=self,
                                                    defaultextension='.pssm', multiple=1,
                                                    filetypes=(
                                                        (('PSSM Files'),
                                                         '.pssm .PSSM'),
                                                        (('CSV Files'),
                                                         '.csv .CSV'),
                                                        (('All files'), '*'),
                                                    ),
                                                    title=('Select pssm files'))
            if filenames:
                filename = filenames[0]
        if filename:
            self.filename = filename

    def createMenuBar(self):
        menu = tk.Menu(self.master)
        self.master.config(menu=menu)

        # file menu
        file = tk.Menu(menu)
        file.add_command(label="Open file", command=self.openfile)
        file.add_command(label="Exit", command=self.quit)
        menu.add_cascade(label="File", menu=file)

        # help menu
        help = tk.Menu(menu)
        help.add_command(label="About", command=self.aboutDialog)
        menu.add_cascade(label="Help", menu=help)

    def openfile(self):
        filenames = filedialog.askopenfilenames(master=self,
                                                defaultextension='.pssm', multiple=1,
                                                filetypes=(
                                                    (('PSSM Files'),
                                                     '.pssm .PSSM'),
                                                    (('CSV Files'),
                                                     '.csv .CSV'),
                                                    (('All files'), '*'),
                                                ),
                                                title=('Select pssm files'))
        if filenames:
            filename = filenames[0]
        self.filename = filename

    def aboutDialog(self):
        messagebox.showinfo(
            "About", "{} v{}\n\nAuthor : Rosdyana Kusuma".format(PROGNAME, VERSION))

    def makeform(self, root, fields):
        entries = []
        for field in fields:
            row = tk.Frame(root)
            lab = tk.Label(row, width=15, text=field, anchor='w')
            ent = tk.Entry(row)
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field, ent))
        return entries


def main():
    filename = None
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    app = Application(filename=filename)
    app.master.title("{} v.{}".format(PROGNAME, VERSION))
    app.mainloop()


if __name__ == '__main__':
    main()
