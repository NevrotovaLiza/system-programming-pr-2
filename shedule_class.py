from watchdog.events import FileSystemEventHandler
znach: list = ['а', 'ы', 'у', 'э', 'о', 'я', 'и', 'ю', 'е', 'ё', 'a', 'e', 'i', 'o', 'u']

class FileShedule(FileSystemEventHandler):
    def on_created(self, event):
        file_name: str = event.src_path.split("\\")
        name: str = file_name[-1].split(".")
        name_second: str = name[0]
        name_second.lower()
        for w in name_second:
            if w in znach:
                print(w.upper())
            else:
                print(w.lower())
