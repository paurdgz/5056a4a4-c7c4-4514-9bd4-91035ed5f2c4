/*
 SECTION: Group exercises
 DESCRIPTION: Write a valid SQL query to solve each problem.
 */


-- A) Get all the unique department names.
-- * es seleccionar todas las columnas
SELECT DISTINCT department FROM  course;
-- DISTINCT seleccionar los valores únicos de department


-- B) Get the top 10 female students (first_name, last_name, age, gpa) with the best GPA scores and order by age (asc).
SELECT
	first_name AS "first name",
	last_name AS "Last name",
	age AS "Age",
	gpa AS "GPA"
FROM
	student
WHERE
	gender = 'female' -- aquí se podrían poner diferentes condiciones
ORDER BY
	gpa DESC, -- DESC = Descendiente
	age ASC,
	first_name ASC,
	last_name ASC
LIMIT 10
;


-- C) Count the number of male/female students that are at least 25 years old.
SELECT
	gender AS "Gender",
	count(gender) AS "Count"
FROM
	student
WHERE
	age >= 25
GROUP BY gender
;



-- D) Get the number of male/female students that were accepted
SELECT
    s.gender,
    count(s.gender)
FROM
	student s INNER JOIN enrollment e ON s.id = e.student_id
WHERE
    e.approved = 1
GROUP BY
    s.gender
;

-- E) Get the min, average, and max GPA of the accepted male students that are less than 20 years old.
SELECT
    MIN(s.gpa),
    AVG(s.gpa),
    MAX(s.gpa)
FROM
	student s INNER JOIN enrollment e ON s.id = e.student_id
WHERE
    s.gender='male' AND s.age <= 20 AND e.approved = 1
;

SELECT
    *
FROM
    (
        SELECT
            gender,
            MIN(gpa),
            AVG(gpa),
            MAX(gpa)
        FROM student INNER JOIN enrollment e on student.id = e.student_id
        WHERE student.age <= 20 AND e.approved = 1 AND gender = 'male'
        GROUP BY  gender
        ) gender_aggregate
WHERE
    gender_aggregate.gender = 'male'
;
-- F) Get the number of enrollments to courses that take longer than 2 years to finalize.

SELECT
    count(*)
FROM
    course c INNER JOIN enrollment e on c.id = e.course_id
WHERE c.years > 2 AND e.approved = 1
;
-- G) Get the number of male/female student that will take a course from the 'Statistics' department.

SELECT
    gender,
    c.name,
    count(*)
FROM
    student s
        INNER JOIN enrollment e on s.id = e.student_id
        INNER JOIN  course c on e.course_id = c.id
WHERE
    lower(c.department) LIKE 'stat%s'
GROUP BY
    gender,
    c.name
;

/*
 SECTION: Individual exercises
 DESCRIPTION: Write a valid SQL query to solve each problem.
 */

-- A) COUNT THE NUMBER OF COURSES PER DEPARTMENT
SELECT department,
count(department)
FROM
	course
GROUP BY department
;

--B) HOW MANY MEN/FEMALE STUDENT WHERE ACCEPTED
SELECT
    s.gender,
    count(s.gender)
FROM
	student s INNER JOIN enrollment e ON s.id = e.student_id
WHERE
    e.approved = 1
GROUP BY
    s.gender
;

--C) HOW MANY STUDENTS WHERE ACCEPTED PEAR COURSE
SELECT
    student_id,
    c.name,
    count(*)
FROM
    student s
        INNER JOIN enrollment e on s.id = e.student_id
        INNER JOIN  course c on e.course_id = c.id

GROUP BY
    course,
    c.name
;

-- D) What's the average age and gpa per course?
SELECT
    name,
    avg(gpa),
    avg(age)
FROM
    student INNER JOIN enrollment  on student.id = enrollment.student_id
    INNER JOIN course on course.id = enrollment.course_id
GROUP BY
    course.name
;

-- E) Get the average number of years the enrolled (approved) female student will study.
SELECT
    gender,
    AVG(years)
FROM
    student INNER JOIN enrollment ON student.id = enrollment.student_id
    INNER JOIN course ON course.id = enrollment.course_id
WHERE
    enrollment.approved = 1 AND gender = 'female'
GROUP BY
    student.gender
;