from collections import Counter

class SimpleBPETokenizer:
    def __init__(self):
        # 256 basic byte tokens (0-255) + learned merged tokens
        self.merges = {}  # maps (int, int) -> int (new token id)
        self.vocab = {}   # maps int -> bytes (for decoding)
        self._reset_vocab()

    def _reset_vocab(self):
        # Initialize the base vocabulary with standard single-byte values
        self.vocab = {i: bytes([i]) for i in range(256)}

    def _get_stats(self, ids):
        # Count frequencies of all adjacent pairs
        counts = Counter()
        for pair in zip(ids, ids[1:]):
            counts[pair] += 1
        return counts

    def _merge(self, ids, pair, idx):
        # Replace occurrences of 'pair' in the list with 'idx'
        new_ids = []
        i = 0
        while i < len(ids):
            if i < len(ids) - 1 and (ids[i], ids[i+1]) == pair:
                new_ids.append(idx)
                i += 2
            else:
                new_ids.append(ids[i])
                i += 1
        return new_ids

    def train(self, text, vocab_size):
        assert vocab_size >= 256
        num_merges = vocab_size - 256
        
        # Step 1: Convert raw string to UTF-8 bytes representation
        text_bytes = text.encode("utf-8")
        ids = list(text_bytes)
        
        self.merges = {}
        self._reset_vocab()

        # Step 2: Iteratively find and merge the most frequent pairs
        for i in range(num_merges):
            stats = self._get_stats(ids)
            if not stats:
                break  # No more pairs left to merge
                
            # Find the most frequent pair
            top_pair = max(stats, key=stats.get)
            new_id = 256 + i
            
            # Record the merge rule
            ids = self._merge(ids, top_pair, new_id)
            self.merges[top_pair] = new_id
            self.vocab[new_id] = self.vocab[top_pair[0]] + self.vocab[top_pair[1]]
            
            print(f"Merge {i+1}/{num_merges}: {top_pair} -> {new_id}")

    def encode(self, text):
        # Convert unseen text to base bytes
        ids = list(text.encode("utf-8"))
        
        # Apply learned merges in the exact chronological order they were trained
        while len(ids) >= 2:
            stats = self._get_stats(ids)
            # Find which of the available pairs in the text has the lowest merge rank
            # (meaning it was merged first during training)
            pair = min(stats, key=lambda p: self.merges.get(p, float('inf')))
            
            if pair not in self.merges:
                break  # No more valid merge rules apply
                
            ids = self._merge(ids, pair, self.merges[pair])
        return ids

    def decode(self, ids):
        # Concatenate byte fragments and decode safely back to text
        text_bytes = b"".join(self.vocab[idx] for idx in ids)
        return text_bytes.decode("utf-8", errors="replace")
# Sample corpus
training_text = "tokenization is essential for language models. tokenization breaks text into pieces."

tokenizer = SimpleBPETokenizer()

# Train to a tiny vocabulary size of 260 tokens (4 merges over base 256)
tokenizer.train(training_text, vocab_size=260)

# Test encoding and decoding on new text
test_text = "tokenization breaks text!"
encoded = tokenizer.encode(test_text)
decoded = tokenizer.decode(encoded)

print("\n--- Evaluation ---")
print(f"Original Text: {test_text}")
print(f"Encoded Token IDs: {encoded}")
print(f"Decoded Output: {decoded}")
print(f"Successful Roundtrip? {test_text == decoded}")

