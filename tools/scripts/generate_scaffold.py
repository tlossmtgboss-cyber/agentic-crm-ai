#!/usr/bin/env python3
import os, json, requests, argparse
from git import Repo

def call_openai(prompt):
    headers = {"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an AI assistant generating repository files in JSON format."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }
    res = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    return res.json()

def write_files(repo_path, files):
    for f in files:
        path = os.path.join(repo_path, f["path"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as out:
            out.write(f["content"])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    parser.add_argument("--branch", default="ai-scaffold")
    args = parser.parse_args()

    repo = Repo(os.getcwd())
    prompt = f"Generate code/files for: {args.task}. Return JSON list: [{{'path': 'file/path', 'content': '...'}}]"
    result = call_openai(prompt)
    content = result["choices"][0]["message"]["content"]

    files = json.loads(content.strip())
    write_files(os.getcwd(), files)

    branch = repo.create_head(args.branch)
    repo.git.checkout(branch)
    repo.git.add(all=True)
    repo.index.commit(f"[ai] {args.task}")
    origin = repo.remotes.origin
    origin.push(branch)

if __name__ == "__main__":
    main()
