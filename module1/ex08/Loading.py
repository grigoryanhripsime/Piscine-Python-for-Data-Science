from os import get_terminal_size


def ft_tqdm(lst: range) -> None:
    """
    This is an implementation of python original tqdm,
    which simple prints out loading bar.
    """

    total_len = len(lst)

    for i, value in enumerate(lst, 1):
        try:
            terminal_width = get_terminal_size().columns
        except OSError:
            terminal_width = 80
        percent = i / total_len
        percent_str = f"{percent * 100:3.0f}%"
        bar_width = max(10, terminal_width - len(percent_str) - 20)
        filled_segment = int(bar_width * percent)
        bar = "=" * filled_segment + " " * (bar_width - filled_segment)
        print(f"\r{percent_str}|{bar}| {i}/{total_len}", end="", flush=True)
        yield value

    print()
