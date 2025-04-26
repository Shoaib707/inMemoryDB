# In-Memory Key-Value Database with Transaction Support

## Requirements
- Python 3.8 or higher

## Installation & Running
1. **Clone** the repo:  
   ```bash
   git clone git@github.com:<your-username>/InMemoryDB.git
   cd InMemoryDB

   Create and activate a virtual environment:
   python3 -m venv venv
  source venv/bin/activate

  Install test dependencies:
  pip install pytest

  Run the built-in smoke test:
  python3 in_memory_db.py


  Future Assignment Improvements
  Honestly, if this were a full-blown course project, I’d love to play around with nested transactions and let us pick different isolation levels so we can actually see how various concurrency models work in practice. It would also be cool to add rollback savepoints, so you could undo just part of a transaction instead of having to scrap everything. To make it even more real-world, I’d throw in a requirement for thread-safety and some basic performance benchmarks—nothing teaches you scale like your code actually slowing to a crawl! And for grading, it’d be awesome if professors checked our test coverage and code style, since that’s exactly what teams do on the job.
