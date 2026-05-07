import os
from pathlib import Path

from django.http import JsonResponse
from django.shortcuts import render
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parent.parent


def get_config_value(name):
    value = os.getenv(name)
    if value:
        return value

    env_file = BASE_DIR / ".env.local"
    if env_file.exists():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, raw_value = stripped.split("=", 1)
            if key.strip() == name:
                return raw_value.strip().strip('"').strip("'")

    return None


def build_client():
    api_key = get_config_value("OPENAI_API_KEY") or get_config_value("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Set OPENAI_API_KEY or OPENROUTER_API_KEY in the environment or .env.local file.")

    base_url = get_config_value("OPENAI_BASE_URL")
    model = get_config_value("OPENAI_MODEL")

    if api_key.startswith("sk-or-v1"):
        base_url = base_url or "https://openrouter.ai/api/v1"
        model = model or "openai/gpt-4o-mini"
        client = OpenAI(api_key=api_key, base_url=base_url)
    else:
        model = model or "gpt-4o-mini"
        client = OpenAI(api_key=api_key)

    return client, model


def get_completion(prompt):
    client, model = build_client()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        max_tokens=400,
    )
    return response.choices[0].message.content.strip()


def query_view(request):
    if request.method == "POST":
        prompt = (request.POST.get("prompt") or "").strip()
        if not prompt:
            return JsonResponse({"response": "Please enter a prompt first."}, status=400)

        try:
            response = get_completion(prompt)
        except Exception as exc:
            return JsonResponse({"response": f"Request failed: {exc}"}, status=500)

        return JsonResponse({"response": response})

    return render(request, "index.html")
