from flask import Flask, jsonify, send_from_directory, request
import subprocess
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Serve UI
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')


# 🔥 Generate API (MULTI-TEMPERATURE)
@app.route('/generate', methods=['GET'])
def generate_text():
    #prompt = request.args.get("prompt", "i am feeling").
    prompt = request.args.get("prompt", "i am feeling").lower()
    # 🎯 temperatures to compare
    temperatures = [0.3, 0.6, 0.65]

    results = {}

    try:
        for temp in temperatures:
            result = subprocess.run(
                [
                    "python", "sample.py",
                    "--out_dir=out-movies",
                    "--start", prompt,
                    "--temperature", str(temp),
                    "--device=cpu"
                ],
                capture_output=True,
                text=True,
                cwd=BASE_DIR
            )

            full_output = result.stdout.strip()

            print(f"\n=== RAW OUTPUT (temp={temp}) ===\n", full_output)

            # ❗ fallback if empty
            if not full_output:
                results[str(temp)] = result.stderr.strip() or "No output"
                continue

            # 🧹 CLEAN OUTPUT
            lines = full_output.split("\n")

            clean_lines = []
            for line in lines:
                line = line.strip()

                if (
                    line.startswith("Overriding")
                    or line.startswith("Loading")
                    or line.startswith("number of parameters")
                    or line == "---------------"
                    or line == ""
                ):
                    continue

                clean_lines.append(line)

            # fallback if cleaned empty
            if not clean_lines:
                final_output = full_output[:500]
            else:
                final_output = "\n".join(clean_lines[:20])

            results[str(temp)] = final_output

        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)