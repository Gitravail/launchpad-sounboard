from app import App
import sounddevice as sd

if __name__ == '__main__':
    print(sd.query_devices())
    app = App(8, 8, sd.default)
