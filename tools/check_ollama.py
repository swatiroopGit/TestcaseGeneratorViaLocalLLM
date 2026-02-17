import ollama
import sys
import time

def check_ollama(model_name="llama3.2"):
    print(f"[Checking Ollama connection...]")
    try:
        # Check connection by listing models
        try:
            models_response = ollama.list()
            print("[CONNECTED] Connected to Ollama!")
        except Exception as e:
            print(f"[ERROR] Could not connect to Ollama. Make sure 'ollama serve' is running.")
            print(f"Error: {e}")
            sys.exit(1)
        
        # Check if model exists
        available_models = [m['model'] for m in models_response.get('models', [])]
        print(f"[INFO] Available models: {available_models}")

        model_found = False
        for m in available_models:
            if model_name in m:
                model_found = True
                print(f"[FOUND] Model '{model_name}' found: {m}")
                break
        
        if not model_found:
            print(f"[MISSING] Model '{model_name}' NOT found locally.")
            print(f"[PULLING] Pulling model '{model_name}'... (This may take a while)")
            try:
                # Stream the pull progress
                current_digest = None
                # Note: ollama.pull returns a generator if stream=True
                resp = ollama.pull(model_name, stream=True)
                for progress in resp:
                    status = progress.get('status', '')
                    completed = progress.get('completed', 0)
                    total = progress.get('total', 1)
                    
                    if status == "pulling manifest":
                         print(f"   [Pulling Manifest] {status}")
                    elif "downloading" in status:
                         percent = (completed / total) * 100 if total else 0
                         sys.stdout.write(f"\r   [Downloading] {percent:.1f}%")
                         sys.stdout.flush()
                    elif status == "verifying sha256 digest":
                         print(f"\n   [Verifying] {status}")
                    elif status == "writing manifest":
                         print(f"   [Writing Manifest] {status}")
                         
                print("\n[pulled] Model pulled successfully!")
            except Exception as e:
                print(f"\n[ERROR] Failed to pull model: {e}")
                sys.exit(1)
            
        print(f"[VERIFYING] Verifying generation with '{model_name}'...")
        start_time = time.time()
        try:
            response = ollama.chat(model=model_name, messages=[
                {'role': 'user', 'content': 'Respond with "System Online" only.'}
            ])
        except Exception as e:
            print(f"[ERROR] Generation failed: {e}")
            sys.exit(1)

        duration = time.time() - start_time
        
        content = response['message']['content'].strip()
        print(f"[RESPONSE] {content}")
        print(f"[TIME] {duration:.2f}s")
        
        if "System Online" in content or len(content) > 0:
            print("\n[SUCCESS] Link Verified! The system is ready for Phase 3.")
        else:
            print("\n[WARNING] Unexpected response content.")
            
    except Exception as e:
        print(f"\n[ERROR] Link Broken.")
        print(f"Details: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_ollama()
