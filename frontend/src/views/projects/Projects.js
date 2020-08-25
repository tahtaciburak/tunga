import React from 'react'
import {
    CCol, CBadge,
    CCard,
    CCardBody,
    CCardHeader,
    CDataTable,
    CButton
} from '@coreui/react'
import usersData from '../users/UsersData'


const fields = ['name', 'registered', 'role', 'status']

const getBadge = status => {
    switch (status) {
        case 'Active':
            return 'success'
        case 'Inactive':
            return 'secondary'
        case 'Pending':
            return 'warning'
        case 'Banned':
            return 'danger'
        default:
            return 'primary'
    }
}

class Projects extends React.Component {
    render() {
        return (
            <>
                <div className="card">
                    <div className="card-header">
                        Projects
                    </div>
                    <div className="card-body">
                        <CCol xs="12" lg="12">
                            <CCard>
                                <CCardHeader>
                                    <CButton color="success">New Project</CButton>
                                    <CButton color="success">New Project2</CButton>
                                </CCardHeader>
                                <CCardBody>
                                    <CDataTable
                                        items={usersData}
                                        fields={fields}
                                        striped
                                        itemsPerPage={5}
                                        pagination
                                        scopedSlots={{
                                            'status':
                                                (item) => (
                                                    <td>
                                                        <CBadge color={getBadge(item.status)}>
                                                            {item.status}
                                                        </CBadge>
                                                    </td>
                                                )

                                        }}
                                    />
                                </CCardBody>
                            </CCard>
                        </CCol>
                    </div>
                </div>
            </>
        )
    }
}

export default Projects
