import tkinter as tk
from tkinter import ttk
import unittest


class TKinterTestCase(unittest.TestCase):
    """These methods are going to be the same for every GUI test,
    so refactored them into a separate class
    """
    def setUp(self):
        self.root = tk.Tk()
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        # Loop to handle Tkinter events without freezing
        self.root.update_idletasks()
        self.root.update()


class TestViewAskText(TKinterTestCase):
    def test_enter(self):
        v = View_AskText(self.root, value="йцу")
        self.pump_events()
        v.e.focus_set()
        v.e.insert(tk.END, 'кен')
        v.e.event_generate('<Return>')
        self.pump_events()

        with self.assertRaises(tk.TclError):
            v.top.winfo_viewable()
        self.assertEqual(v.value, 'йцукен')


# ###########################################################
# The class being tested (normally, it's in a separate module
# and imported at the start of the test's file)
# ###########################################################

class View_AskText:
    def __init__(self, master, value=""):
        self.value = None

        top = self.top = tk.Toplevel(master)
        top.grab_set()
        self.l = ttk.Label(top, text="Value:")
        self.l.pack()
        self.e = ttk.Entry(top)
        self.e.pack()
        self.b = ttk.Button(top, text='Ok', command=self.save)
        self.b.pack()

        if value:
            self.e.insert(0, value)
        self.e.focus_set()
        top.bind('<Return>', self.save)

    def save(self, *_):
        self.value = self.e.get()
        self.top.destroy()


if __name__ == '__main__':
    # unittest.main()
    root = tk.Tk()
    v = View_AskText(root, value="йцу")
    root.wait_window(v.top)
    root.mainloop()
