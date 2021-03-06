(defun reverse-if-list (item)
  (if (listp item)
      (reverse item)
      item))

(defun reverse-state (state)
  (map 'list #'reverse-if-list state))

(setq max_height (read))
(write max_height)
(write-line "")
(setq initial_state (read))
(write (reverse-state initial_state))
(write-line "")
(setq goal_state (read))
(write (reverse-state goal_state))
