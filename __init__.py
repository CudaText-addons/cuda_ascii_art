from cudatext import *
import sys
import os

sys.path.append(os.path.dirname(__file__))
from .pyfiglet import Figlet

config_filename = os.path.join(app_path(APP_DIR_SETTINGS), 'plugins.ini')
config_section = 'ascii_art'

class Command:
    op_font='slant'
    op_direction='auto'
    op_justify='auto'
    op_width='80'
    
    def ini_get(self):
        self.op_font      = ini_read(config_filename, config_section, 'font', self.op_font)
        self.op_direction = ini_read(config_filename, config_section, 'direction', self.op_direction)
        self.op_justify   = ini_read(config_filename, config_section, 'justify', self.op_justify)
        self.op_width     = ini_read(config_filename, config_section, 'width', self.op_width)

    def ini_set(self):
        ini_write(config_filename, config_section, 'font', self.op_font)
        ini_write(config_filename, config_section, 'direction', self.op_direction)
        ini_write(config_filename, config_section, 'justify', self.op_justify)
        ini_write(config_filename, config_section, 'width', self.op_width)
        
    def preview(self):
        self.ini_get()
        msg = 'Some Text'
        file_open('')
        eol = '\n'
        dirs = self.fonts()
        text = ''
        for (i, afont) in enumerate(dirs):
            msg_status('Preview fonts: %d / %d' % (i+1, len(dirs)), True)
            f = Figlet(font=afont, direction=self.op_direction, justify=self.op_justify, width=int(self.op_width))
            text += 'Font: '+afont+eol+f.renderText(msg)+eol+eol
        ed.insert(0, 0, text)

    def render(self):
        self.ini_get()
        f = Figlet(font=self.op_font, direction=self.op_direction, justify=self.op_justify, width=int(self.op_width))
        text = dlg_input('Text:', '')
        if text:
            text = f.renderText(text)
            x, y, endx, endy = ed.get_carets()[0]
            if x > 0:
                ed.insert(x, y, '\n')
                x = 0
                y += 1
            ed.insert(x, y, text)
            msg_status('Text inserted')

    def fonts(self):
        dir = os.path.join(os.path.join(os.path.dirname(__file__), 'pyfiglet'), 'fonts')
        dirs = os.listdir(dir)
        dirs = [d[:-4] for d in dirs if d.endswith('.flf')]
        return sorted(dirs)

    def config_font(self):
        dirs = self.fonts()
        num = dlg_menu(DMENU_LIST, dirs)
        if num is None:
            return
        self.ini_get()
        self.op_font = dirs[num]
        msg_status('Selected font: '+self.op_font)
        self.ini_set()
        self.render()

    def config_all(self):
        self.ini_get()
        self.ini_set()
        if os.path.isfile(config_filename):
            file_open(config_filename)
            lines = [ed.get_text_line(i) for i in range(ed.get_line_count())]
            try:
                index = lines.index('['+config_section+']')
                ed.set_caret(0, index)
            except:
                pass
