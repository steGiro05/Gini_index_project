import subprocess

def run_script(script_path):
    print(f"Running: {script_path}")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error in {script_path}:\n{result.stderr}")
        raise RuntimeError(f"Script {script_path} failed")
    else:
        print(f"Completed: {script_path}\n{result.stdout}")

def main():
    try:
        # Education Level Section
        run_script("split.py")                      # Step 1
        run_script("gini_index.py")                 # Step 2-3
        run_script("avg.py")                        # Step 3-2

        # Years of Experience Section
        run_script("quartiles.py")                                         # Step 1
        run_script("quartiles/add_cumulative_percentage.py")              # Step 2
        run_script("quartiles/gini_per_quartille.py")                     # Step 3-4
        run_script("quartiles/avg.py")                                     # Step 4-3

        print("All scripts executed successfully.")
    except Exception as e:
        print(f"Process terminated: {e}")

if __name__ == "__main__":
    main()
