device_names = {1: 'cpu0', 2: 'mem_bank0', 3: 'mem_bank1'}
device_models = {1: "Xeon", 2: 'Corsair', 3: 'Corsair'}

all_devices = []

for id, name in device_names.items():
    model = device_models[id]
    all_devices.append({'id': id, 'name': name, 'model': model})

print(all_devices)

models_device = {}

for id, model in device_models.items():
    if model in models_device:
        models_device[model].append(device_names[id])
    else:
        models_device[model] = device_names[id]

print(models_device)