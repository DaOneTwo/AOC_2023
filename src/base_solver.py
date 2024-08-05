from pathlib import Path


class BaseSolver:
    def __init__(self, input_path: str):
        self.input_path = Path(input_path)

    def input_line_by_line(self) -> str:
        """read and return lines from the input file 1 at a time."""
        with open(self.input_path, 'r') as file:
            line = file.readline()
            while line:
                yield line.strip()
                line = file.readline()

    def input_chunked(self, chunk_size: int) -> list[str]:
        with open(self.input_path, 'r') as file:
            chunk = []
            for line in file.readline():
                chunk.append(line)
                if len(chunk) == chunk_size:
                    yield chunk
                    chunk = []
            if chunk:
                yield chunk

    def input_all_lines(self) -> list[str]:
        return self.input_path.read_text().splitlines()

    def solve_pt1(self):
        raise NotImplemented('Part 1 solver not implemented')

    def solve_pt2(self):
        raise NotImplemented('Part 2 solver not implemented')

