import unittest

from classified_email_program import sanitize_user_words, censor_email_text, create_menu_with_options, process_user_menu_input


class ClassifiedEmailTest(unittest.TestCase):
    def test_sanitize_user_words_splits_string_and_strips_leading_and_trailing_whitespace(self):
        self.assertEqual(sanitize_user_words("score # four# set forth "), ['score','four','set forth'], "Should be ['score','four','set forth']")

    def test_censor_email_text_replace_words_with_asterisks(self):
        email_text = "These words."
        classified_words = ['words']
        self.assertEqual(censor_email_text(email_text, classified_words)['email'], "These *****.",
        "Should be 'These *****.'")

    def test_censor_email_text_replace_no_words_with_asterisks(self):
        email_text = "These words."
        classified_words = ['skywalker']
        self.assertEqual(censor_email_text(email_text, classified_words)['email'], "These words.",
        "Should be 'These words.'")

    def test_censor_flag_true(self):
        email_text = "These words."
        classified_words = ['words']
        self.assertEqual(censor_email_text(email_text, classified_words)['flag'],True, 
        "Should be True")

    def test_censor_flag_false(self):
        email_text = "These words."
        classified_words = ['skywalker']
        self.assertEqual(censor_email_text(email_text, classified_words)['flag'],False, 
        "Should be False")

    def test_menu_options_size(self):
        menu = create_menu_with_options()
        self.assertEqual(len(menu), 4,
        "Should be 4.")

    def test_menu_options_has_correct_keys(self):
        menu = create_menu_with_options()
        keys = list(menu.keys())
        target_keys = ['1','2','3','4']
        self.assertEqual(keys, target_keys,
        "Should be ['1','2','3','4']")

    def test_menu_has_correct_values(self):
        menu = create_menu_with_options()
        values = list(menu.values())
        target_values = [" Display preloaded sample text.",
        " Run censor function with preloaded sample text and new user provided classified words.",
        " Run censor function with new user provided text and new user provided classified words.",
        " Exit program."]
        self.assertEqual(values, target_values,
        ("Should be ", target_values))
    
    def test_process_user_input_for_value_4(self):
        ans = '4'
        self.assertEqual(process_user_menu_input(ans), False,
        "Should be False.")



if __name__ == '__main__':
    unittest.main()