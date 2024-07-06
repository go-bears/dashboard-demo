import subprocess


def run_streamlit_app():
    command = ["streamlit", "run", "streamlit_app.py"]
    subprocess.run(command)

if __name__ == "__main__":
    run_streamlit_app()
