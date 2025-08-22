
**Proposal Plan for Comic's Log API**

**Description:**
This API lets a comedian log materials (jokes), plan ordered set lists and track on stage performance feedback to help improve and polish their materials/sets.

**Create:**
- Add new users (email, password_hash, stage_name)Add new materials (title, status (ENUM): 'draft'/'working'/'polished', approx_duration_sec, notes)
- Add new on_stage_performances (name, venue_id, slot_minutes, self_rating, approx_audience_count, feedback_comments, performed_at)
- Add new venues (name, location)
- Add set_list_items to a performance (on_stage_performance_id, material_id, list_order, item_duration_sec, tried, material_rating, comments)

**Read:**
- Query materials (eg. filter by status or search by title)
- Retrieve on_stage_performances
- Retrieve set list for a performance (ordered items + total_duration_sec)
- Retrieve venues list (name, location)

**Update:**
- Update material (title, status, approx_duration_sec, notes)
- Update on_stage_performance (name, venue_id, slot_minutes, self_rating, approx_audience_count, feedback_comments, performed_at)
- Update set_list_item (list_order, item_duration_sec, tried, material_rating, comments)
- Update venue (name, location)

**Delete:**
- Delete a material
- Delete an on_stage_performance
- Delete a set_list_item from a performance
- Delete a venue
