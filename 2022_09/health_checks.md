

https://sreuniversity.in/health-check/


queue depth .... queue growing, queue shrinking ... cli to interrogate queue depth, dynamics


https://netflixtechblog.com/linux-performance-analysis-in-60-000-milliseconds-accc10403c55

brendan gregg ... at netflix:
o
uptime
dmesg | tail
vmstat 1
mpstat -P ALL 1
pidstat 1
iostat -xz 1
free -m
sar -n DEV 1
sar -n TCP,ETCP 1
top
