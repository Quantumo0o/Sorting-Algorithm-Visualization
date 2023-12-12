# Sorting Algorithm Visualization

This repository contains Python code to visualize various sorting algorithms using Matplotlib and OpenCV. Each sorting algorithm is implemented as a function that generates images at each step of the sorting process, and these images are then combined into a video using OpenCV.

## Table of Contents

- [Sorting Algorithms](#sorting-algorithms)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Sorting Algorithms

The following sorting algorithms are implemented and visualized in this repository:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Heap Sort
- Radix Sort

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Quantumo0o/Sorting-Algorithm-visualization.git
   ```

2. Navigate to the project directory:

   ```bash
   cd sorting-algorithm-visualization
   ```

3. Install the required Python libraries:

   ```bash
   pip install opencv-python matplotlib numpy
   ```

## Usage

1. To visualize a sorting algorithm, open the corresponding Python script (e.g., `bubble_sort.py`, `selection_sort.py`, etc.) in your preferred code editor.

2. Modify the input data or algorithm parameters as needed.

3. Run the script:

   ```bash
   python bubble_sort.py
   ```

   This will generate a series of images in the project directory, representing the steps of the sorting algorithm.

4. Once the script has completed, you can use the following OpenCV script to create a video from the generated images:

   ```bash
   python create_video.py
   ```

   The video will be saved as `output_video.mp4`.

## Examples

To see examples of the sorting algorithms in action, you can check the following files in the repository:

- `bubble_sort.py`
- `selection_sort.py`
- `insertion_sort.py`
- `merge_sort.py`
- `heap_sort.py`
- `radix_sort.py`

Each of these files contains an example of how to use and visualize the corresponding sorting algorithm.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix:

   ```bash
   git checkout -b feature-name
   ```

3. Make your changes and commit them:

   ```bash
   git commit -m "Description of your changes"
   ```

4. Push your changes to your fork:

   ```bash
   git push origin feature-name
   ```

5. Create a pull request on the original repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
