from src.gui.app import MainApp
from src.model.classes.DB.database import Base, engine

Base.metadata.create_all(engine)

def main():
    print("Iniciando la interfaz gráfica...")
    MainApp().run()

if __name__ == "__main__":
    main()