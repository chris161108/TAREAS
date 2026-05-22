import math

def validador_red():
    ips = [(192, 168, 1, 1), (10, 0, 0, 255), (172, 16, 255, 0), (8, 8, 8, 8)]
    prohibidos = {0, 255}
    clasificacion = {}
    
    for ip in ips:
        valida = True
        for octeto in ip:
            if octeto in prohibidos:
                valida = False
                break
                
        if valida:
            peso = math.log(sum(ip))
            clasificacion[ip] = {"valida": True, "peso": round(peso, 2)}
        else:
            clasificacion[ip] = {"valida": False, "peso": 0.0}
            
    return clasificacion

print(f"8️⃣ Red -> Clasificación: {validador_red()}")