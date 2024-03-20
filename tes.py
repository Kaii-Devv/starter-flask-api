def find_nearest_divisible_by_eight(n):
    # Fungsi ini mencari bilangan terdekat yang habis dibagi 8
    return 8 * round(n/8)

def get_size(aspect_ratio_string):
    # Set default
    width = 512
    height = 512

    # Get aspect ratio

    if aspect_ratio_string != '1:1':
        aspect_ratio_array = aspect_ratio_string.split(':')
        aspect_ratio = int(aspect_ratio_array[0]) / int(aspect_ratio_array[1])

        # Adjust base size for 1:4 and 4:1 aspect ratios. Use @aspect_ratio_string, not @aspect_ratio, to avoid precision errors.
        short_size = 512 if aspect_ratio_string in ['4:1', '1:4'] else 512

        # Use landscape?
        if aspect_ratio > 1:
            height = short_size
            width = find_nearest_divisible_by_eight(round(short_size * aspect_ratio))

        # Nope, set to portrait.
        else:
            width = short_size
            height = find_nearest_divisible_by_eight(round(width / aspect_ratio))

    max_size = max(width, height)

    return {
        'width': width,
        'height': height,
        'max': max_size
    }
print(get_size("3:2"))
