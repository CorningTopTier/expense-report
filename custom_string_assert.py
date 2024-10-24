from assertpy import add_extension

def is_equal_to_with_diff(self, other_string):
    if self.val != other_string:
        # Provide detailed difference output
        print("Strings are not equal. Showing differences:")
        for i, (char1, char2) in enumerate(zip(self.val, other_string)):
            if char1 != char2:
                print(f"Difference at index {i}: '{char1}' != '{char2}'")
        if len(self.val) != len(other_string):
            print(f"String lengths differ: {len(self.val)} != {len(other_string)}")
    # Continue with the original is_equal_to assertion
    return self.is_equal_to(other_string)

# Register the custom assertion for assertpy
add_extension(is_equal_to_with_diff)