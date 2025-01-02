from metaflow import Flow
run = Flow('ManyKmeansFlow').latest_run
k3 = run.data.top[3]
k4 = run.data.top[4]
k5 = run.data.top[5]
print(k3[0][:3])  # Kata teratas di kluster pertama
