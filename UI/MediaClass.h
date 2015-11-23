#ifndef MEDIACLASS_H
#define MEDIACLASS_H

#include <Python.h>
#include <iostream>
#include <QObject>
#include <stdlib.h>

class MediaClass : public QObject
{
    Q_OBJECT
    Q_PROPERTY(int isComplete READ isComplete)
    Q_PROPERTY(QList<int> status READ status WRITE writeStatus)
    Q_PROPERTY(int winner READ winner)
public:
    MediaClass(QObject *parent = 0):QObject(parent){};

    int isComplete(){
        return complete;
    }

    int winner(){
        return m_winner;
    }

    QList<int> status(){
        return m_status;
    }

    void writeStatus(QList<int> newStatus){
        m_status = newStatus;
    }

    Q_INVOKABLE void nextStep(){
        // Set PYTHONPATH TO working directory
        setenv("PYTHONPATH",".",1);

        PyObject *pName, *pModule, *pDict, *pFunc, *pValue, *presult;


        // Initialize the Python Interpreter
        Py_Initialize();


        // Build the name object
        pName = PyString_FromString((char*)"test_noAlphaBeta");

        // Load the module object
        pModule = PyImport_Import(pName);

        // pDict is a borrowed reference
        pDict = PyModule_GetDict(pModule);

        // pFunc is also a borrowed reference
        pFunc = PyDict_GetItemString(pDict, (char*)"initGame");

        pValue = Py_BuildValue("([i,i,i,i,i,i,i,i,i])",m_status[0], m_status[1], m_status[2], m_status[3], m_status[4], m_status[5], m_status[6], m_status[7], m_status[8]);

        if (PyCallable_Check(pFunc))
        {
            PyErr_Print();
            presult=PyObject_CallObject(pFunc,pValue);
            PyErr_Print();
        } else
        {
            PyErr_Print();
        }

        pValue = Py_BuildValue("()");

        pFunc = PyDict_GetItemString(pDict, (char*)"nextStep");

        if (PyCallable_Check(pFunc))
        {
            PyErr_Print();
            presult=PyObject_CallObject(pFunc,pValue);
            PyErr_Print();
        } else
        {
            PyErr_Print();
        }

        complete = PyLong_AsLong(PyList_GetItem(presult, 0));
        m_winner = PyLong_AsLong(PyList_GetItem(presult, 1));

        for(int i = 2; i < 11; i++){
            auto temp = PyList_GetItem(presult,i);
            m_status[i-2] = PyLong_AsLong(temp);
        }

        Py_DECREF(pValue);

        // Clean up
        Py_DECREF(pModule);
        Py_DECREF(pName);

        // Finish the Python Interpreter
        Py_Finalize();
    }

signals:

public slots:

private:
    int complete = 0;
    QList<int> m_status;
    int m_winner = 0;
};

#endif // MEDIACLASS_H
