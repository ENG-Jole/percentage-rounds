# Percentage Rounds

## About

Silly little Python implementations of [everyone's favorite C# code](https://github.com/MinBZK/woo-besluit-broncode-digid-app/blob/ad2737c4a039d5ca76633b81e9d4f3f9370549e4/Source/DigiD.iOS/Services/NFCService.cs#L182). Turns out a bunch of if-else's is pretty performant in Python.

## Usage

Requires Python 3.10 or greater.
Just run:

```bash
python3 percentage_rounds.py
```

from the directory you cloned this into.

## Benchmark Results

Tested on Python 3.10.3 on a 2021 MacBook Pro 16in with an M1 Pro processor and 16GB of memory:

```bash
If Else: 2.1915992500144057s
Match Case: 2.1753992920275778s
Repeat: 5.820348583976738s
Loop: 6.302988999988884s
Slice: 2.1363271250156686s
```

Initially (and before I upped `timeit` to 5,000,000 iterations) the `match case` implementation was slower than the `if else` implementation, but on several subsequent runs it was faster. No idea why other than mysterious interpreter optimizations I don't really understand and am not planning on digging around to find out.

If you test this on Python 3.11 with similar specs and there's a big delta between my results, please let me know!
