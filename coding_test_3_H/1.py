def count_visible_blocks(blocks):
    if not blocks:
        return 0

    max_height = 0
    visible_count = 0
    real_max_height = max(blocks)  # Find the real maximum height

    # Iterate from right to left
    for block in reversed(blocks):
        if block > max_height:
            visible_count += 1
            max_height = block
            if block == real_max_height:
                break

    return visible_count
