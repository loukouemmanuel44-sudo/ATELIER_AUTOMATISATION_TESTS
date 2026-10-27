from tester.client import APIClient
from tester.tests import run_contract_tests
from storage import save_run

def execute_test_suite():
    # Exemple avec une API publique sans clé (ex: JSONPlaceholder)
    client = APIClient("https://jsonplaceholder.typicode.com")
    result = client.get_endpoint("/posts/1")
    
    assertions = run_contract_tests(result)
    success = all(a["success"] for a in assertions)
    
    run_data = {
        "status_code": result["status_code"],
        "latency_ms": result["latency_ms"],
        "success": 1 if success else 0,
        "error": result["error"]
    }
    
    # Sauvegarde dans SQLite
    save_run(run_data)
    return run_data

if __name__ == "__main__":
    execute_test_suite()
