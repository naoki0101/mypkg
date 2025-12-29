#!/bin/bash
set -euo pipefail

dir=~
[ "${1:-}" != "" ] && dir="$1"

cd "$dir/ros2_ws2025"

colcon build --symlink-install

set +u
source "$dir/ros2_ws2025/install/setup.bash"
set -u

capfile=/tmp/capacity_test
echo 15 > "$capfile"

log=/tmp/mypkg.log
rm -f "$log" /tmp/mon.log /tmp/warn.log

timeout 10 bash -c "
  ros2 run mypkg warning_listener > /tmp/warn.log 2>&1 &
  ros2 run mypkg battery_monitor --ros-args \
    -p battery_path:=$capfile \
    -p warning_threshold:=20.0 > /tmp/mon.log 2>&1 &
  wait
" || true

cat /tmp/mon.log /tmp/warn.log > "$log"

grep -E 'battery_monitor|Battery monitor node started|Battery monitor node started' "$log" > /dev/null
grep -E 'Battery:' "$log" > /dev/null
grep -E 'WARNING' "$log" > /dev/null

echo "OK"
