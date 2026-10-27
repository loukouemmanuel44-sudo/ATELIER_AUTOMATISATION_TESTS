def run_contract_tests(result):
    assertions = []
    
    # 1. Test du statut HTTP (200 attendu)
    status_ok = result["status_code"] == 200
    assertions.append({"test": "Statut HTTP 200", "success": status_ok})

    # 2. Test du Content-Type JSON
    content_type = result["headers"].get("Content-Type", "")
    is_json = "application/json" in content_type
    assertions.append({"test": "Content-Type JSON", "success": is_json})

    # 3. Test de robustesse (pas d'erreur réseau / timeout)
    no_error = result["error"] is None
    assertions.append({"test": "Pas d'erreur réseau / Timeout", "success": no_error})

    return assertions
