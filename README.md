# RealDiff Python sort-stability demo

Three tests exercise a priority-ordered discount selection. The proposed one-file change makes equal-priority ordering deterministic by code: two broad invariants continue to pass while the exact current tie-winner assertion reacts.