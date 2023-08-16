#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def test_spacecraft_control():
    # Test the execute_command function
    initial_pos = (0, 0, 0)
    initial_dir = "N"
    commands = ["f", "r", "u", "b", "l"]

    final_position, final_direction = execute_command(commands, initial_pos, initial_dir)
    expected_position = (0, 1, -1)
    expected_direction = "N"

    assert final_position == expected_position
    assert final_direction == expected_direction

    # Test the user input part
    user_input_values = ["N", "frubl"]
    with unittest.mock.patch('builtins.input', side_effect=user_input_values):
        initial_pos = (0, 0, 0)
        initial_dir = input("Enter initial direction (N/S/W/E):")
        commands = input("Enter commands (f/r/u/b/l without spaces):")

        final_position, final_direction = execute_command(commands, initial_pos, initial_dir)

        assert final_position == expected_position
        assert final_direction == expected_direction

    print("All tests passed!")

if __name__ == "__main__":
    test_spacecraft_control()

