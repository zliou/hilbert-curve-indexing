Author: Zachary Liou

Created: 2023 September 20

# Hilbert Curve Search

This project was created as a way to explore the concept of a
[Hilbert curve](https://en.wikipedia.org/wiki/Hilbert_curve).

The Python script in this repo explores a strategy for grouping/indexing
points of interest in a 2D space along a Hilbert curve.

Given a search point, the script will generate a set of random points and
return nearby points - both along the Hilbert curve and by traditional
Pythagorean proximity. A scatter plot is rendered to visualize the comparison
of both search strategies.

To run the script:
```
python3 hilbert.py
```

