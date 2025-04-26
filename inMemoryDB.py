class InMemoryDB:
    def __init__(self):
        # Main key-value store
        self._store = {}
        # None when no transaction active, dict for uncommitted changes
        self._txn_buffer = None

    def begin_transaction(self):
        """
        Starts a new transaction. Throws RuntimeError if a transaction is already active.
        """
        if self._txn_buffer is not None:
            raise RuntimeError("Transaction already in progress")
        self._txn_buffer = {}

    def put(self, key: str, value: int):
        """
        Puts a key-value pair in the current transaction. 
        Throws RuntimeError if no transaction is active.
        """
        if self._txn_buffer is None:
            raise RuntimeError("No active transaction")
        self._txn_buffer[key] = value

    def get(self, key: str):
        """
        Retrieves the value for a key from the committed store.
        Returns None if the key does not exist. Uncommitted changes are not visible.
        """
        return self._store.get(key)

    def commit(self):
        """
        Commits all changes from the current transaction to the main store.
        Throws RuntimeError if no transaction is active.
        """
        if self._txn_buffer is None:
            raise RuntimeError("No active transaction")
        # Apply all buffered changes
        for k, v in self._txn_buffer.items():
            self._store[k] = v
        # End transaction
        self._txn_buffer = None

    def rollback(self):
        """
        Aborts the current transaction, discarding buffered changes.
        Throws RuntimeError if no transaction is active.
        """
        if self._txn_buffer is None:
            raise RuntimeError("No active transaction")
        # Discard uncommitted changes
        self._txn_buffer = None


if __name__ == "__main__":
    db = InMemoryDB()
    # Fig 2 examples:
    print(db.get("A"))  # None, A not in store
    try:
        db.put("A", 5)
    except RuntimeError as e:
        print("Expected error:", e)

    db.begin_transaction()
    db.put("A", 5)
    print(db.get("A"))  # None, uncommitted
    db.put("A", 6)
    db.commit()

    print(db.get("A"))  # 6, committed
    try:
        db.commit()
    except RuntimeError as e:
        print("Expected error:", e)
    try:
        db.rollback()
    except RuntimeError as e:
        print("Expected error:", e)

    print(db.get("B"))  # None, B not in store
    db.begin_transaction()
    db.put("B", 10)
    db.rollback()
    print(db.get("B"))  # None, rolled back
