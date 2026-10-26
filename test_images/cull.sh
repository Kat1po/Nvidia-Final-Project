find . -mindepth 1 -type d | while read -r dir; do

    total_files=$(ls -1p | grep -v / | wc -l)
    half_files=$((total_files/2))

    if [ "$half_files" -gt 0 ]; then
        find "$dir" -maxdepth 1 -type f | shuf -n $half_files | xargs -d '\n' rm
    fi
done